# coding:utf-8
from gevent import monkey; monkey.patch_all()
import sys
import os
sys.path.append(os.getcwd()+'/lib')
import sqlite3
import socket
import time
import platform
import signal
import uuid
import shutil
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response, jsonify
from contextlib import closing
import subprocess
from flask_socketio import SocketIO, emit
import json
import xml.etree.ElementTree as ET
from threading import Lock, Thread
import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
from interface import *
from task import *


# 配置
DATABASE = 'web.db'
SECRET_KEY = 'zhouqiang'
USERNAME = 'admin'
PASSWORD = '123'
# 推送线程和锁和队列
thread = None
thread_lock = Lock()
push_list = []
# 自动化任务
handle = {}
# 数据库初始化
c = sqlite3.connect('web.db')
c.execute('update interf_task set status=2;')
c.execute('update push set status=0, conn_num=0;')
c.commit()
c.close()
# 日志清空
try:
    for elem in os.listdir('log/'):
        os.remove('log/'+elem)
except:
    pass


# 创建app
app = Flask(__name__)
app.config.from_object(__name__)
socketio = SocketIO(app)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read().decode('utf-8'))
        db.commit()


def xml_parse(father, page_tree, flag=1):
    if flag:
        for child in father:
            try:
                tag_attr = child.attrib['xpath']
            except:
                tag_attr = ''
            if child.text is None or '\n' in child.text:
                tag_text = ''
            else:
                tag_text = child.text
            page_tree[child.tag] = [tag_attr, tag_text, {}]
            xml_parse(child, page_tree[child.tag][2], flag=1)
    else:
        for child in father:
            tag_attr = child.attrib
            tag_text = child.text
            page_tree[child.tag] = [tag_attr, tag_text, {}]
        try:
            page_tree['step'][2]['elem'] = []
            for elem in father.find('step').iter('elem'):
                page_tree['step'][2]['elem'].append([elem.attrib, elem.text])
        except:
            pass


def write_xml(xml_file, data, flag=1):
    if flag:
        file_name = '../page/' + xml_file + '.xml'
        tree = ET.parse(file_name)
        root = tree.getroot()
        add_row = json.loads(data[0])
        for elem in add_row:
            elem['position'].reverse()
            location = '.'
            for i in elem['position'][:-1]:
                location = location + '/' + i.split('>')[0]
            fa = root.find(location)
            ET.SubElement(fa, elem['data']['tag'])
            child = fa.find(elem['data']['tag'])
            child.text = elem['data']['text']
            child.set('xpath', elem['data']['xpath'])
        del_row = json.loads(data[1])
        del_row.reverse()
        for elem in del_row:
            elem['position'].reverse()
            location = '.'
            for i in elem['position'][:-1]:
                location = location + '/' + i.split('>')[0]
            fa = root.find(location)
            child = root.find(location + '/' + elem['position'][-1])
            fa.remove(child)
        modify = json.loads(data[2])
        modify.reverse()
        for elem in modify:
            elem['position'].reverse()
            location = '.'
            for i in elem['position']:
                location = location + '/' + i.split('>')[0]
            fa = root.find(location)
            if 'text' in elem['data']:
                fa.text = elem['data']['text']
            if 'xpath' in elem['data']:
                fa.set('xpath', elem['data']['xpath'])
            if '>' in elem['position'][-1]:
                fa.tag = elem['position'][-1].split('>')[1]
    else:
        file_name = '../model/' + xml_file + '.xml'
        tree = ET.parse(file_name)
        root = tree.getroot()
        add_row = json.loads(data[0])
        for elem in add_row:
            if elem['position'] == '/':
                ET.SubElement(root, elem['data']['tag'])
                child = root.find(elem['data']['tag'])
                child.text = elem['data']['text']
            else:
                elem_index = int(elem['position'])
                fa = root.find('step')
                fa.insert(elem_index, ET.Element('elem'))
                fa[elem_index].text = elem['data']['text']
                for key in elem['data']['attr']:
                    fa[elem_index].attrib[key] = elem['data']['attr'][key]
        modify = json.loads(data[1])
        modify.reverse()
        for elem in modify:
            try:
                elem_index = int(elem['position'])
                obj = root.find('step')[elem_index]
                for key in elem['data']:
                    if key == 'attr':
                        for ke in elem['data']['attr']:
                            obj.attrib[ke] = elem['data']['attr'][ke]
                    elif key == 'text':
                        obj.text = elem['data']['text']
            except:
                obj = root.find(elem['position'].split('>')[0])
                for key in elem['data']:
                    if key == 'attr':
                        for ke in elem['data']['attr']:
                            obj.attrib[ke] = elem['data']['attr'][ke]
                    elif key == 'text':
                        obj.text = elem['data']['text']
                    else:
                        obj.tag = elem['data']['tag']
        del_row = json.loads(data[2])
        del_row.reverse()
        for elem in del_row:
            try:
                elem_index = int(elem['position'])
                root.find('step').remove(root.find('step')[elem_index])
            except:
                root.remove(root.find(elem['position']))
    tree.write(file_name)


@socketio.on('connect', namespace='/task_refresh')
def ws_connect():
    global push_list, thread
    push_list.append(1)
    # print('Client connected', push_list, thread)
    with thread_lock:
        if thread == None:
            thread = socketio.start_background_task(target=push)


@socketio.on('disconnect', namespace='/task_refresh')
def ws_disconnect():
    global push_list
    push_list.pop()
    # print('Client disconnected', push_list, thread)


def push():
    global push_list, thread
    while True:
        # print('push...', push_list)
        s = connect_db()
        msg = s.execute('select * from tasks order by id desc').fetchall()
        s.close()
        socketio.emit('rec_push', {'code': 200, 'msg': json.dumps(msg)}, namespace='/task_refresh')
        socketio.sleep(3)
        if len(push_list) == 0:
            thread = None
            return



@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    try:
        g.db.close()
    except:
        pass


# 首页
@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return redirect(url_for('api_record'))


# 展示所有任务
@app.route('/task')
def show_tasks():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    tasks = g.db.execute('select * from tasks order by id desc').fetchall()
    case_sets = g.db.execute('select name from case_set order by id desc').fetchall()
    return render_template('show_tasks.html', task=tasks, case_set=case_sets)
    

# 登陆
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('用户名不存在', 'danger')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('密码不正确', 'danger')
        else:
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('login.html', menu='none')


# 注销
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('注销成功', 'info')
    return redirect(url_for('login'))


# 新建自动化任务
@app.route('/add', methods=['POST'])
def add_tasks():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.form['select_set'] == 'none' or request.form['name'] == '':
        flash('任务名或用例集不能为空', 'danger')
        return redirect(url_for('show_tasks'))
    if (request.form['name'],) in g.db.execute('select name from tasks').fetchall():
        flash('任务名不能重复', 'danger')
        return redirect(url_for('show_tasks'))
    try:
        if (int(request.form['name']),) in g.db.execute('select name from tasks').fetchall():
            flash('任务名不能重复', 'danger')
            return redirect(url_for('show_tasks'))
    except:
        pass
    total_num = g.db.execute('select case_num from case_set where name=(?)',
                             [request.form['select_set']]).fetchall()[0][0]
    g.db.execute('insert into tasks (name,case_set,create_time,total_num) values (?,?,?,?)', [request.form['name'],
                 request.form['select_set'], time.strftime('%y%m%d %H:%M', time.localtime()), total_num])
    g.db.commit()
    flash('新任务创建成功', 'success')
    return redirect(url_for('show_tasks'))


# 用例集展示页面
@app.route('/case_set')
def case_set():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    try:
        g.db.execute('create table model_case (id integer\
                     primary key autoincrement,name string not null);')
        g.db.execute('create table tmp_case (id integer primary key \
                     autoincrement,name string not null,case_num string not null);')
        for elem in os.listdir('../model/'):
            if elem == 'login.xml' or elem == 'menu.xml':
                continue
            else:
                g.db.execute('insert into model_case (name) values (?)', [elem.replace('.xml', '')])
        g.db.commit()
    except:
        pass
    model_case = g.db.execute('select * from model_case order by id').fetchall()
    tmp_case = g.db.execute('select * from tmp_case order by id').fetchall()
    case_sets = g.db.execute('select * from case_set order by id').fetchall()
    return render_template('case_set.html', model_case=model_case, tmp_case=tmp_case,
                           case_set=case_sets)
    

@app.route('/add_case', methods=['POST', 'GET'])
def add_case():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        g.db.execute('insert into tmp_case (name, case_num) values (?, ?)',
                     [request.form['name'], (request.form['case_num'])])
        g.db.commit()
        flash('添加成功', 'success')
        return redirect(url_for('case_set'))


@app.route('/del_case', methods=['POST'])
def del_case():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    g.db.execute('delete from tmp_case where name=(?)', [request.form['name']])
    g.db.commit()
    flash('移除成功', 'success')
    return redirect(url_for('case_set'))


@app.route('/add_set', methods=['POST'])
def add_set():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.form['cname'] == '':
        flash('用例集名称不能为空', 'danger')
        return redirect(url_for('case_set'))
    if (request.form['cname'],) in g.db.execute('select name from case_set').fetchall():
        flash('用例集名称不能重复', 'danger')
        return redirect(url_for('case_set'))
    try:
        if (int(request.form['cname']),) in g.db.execute('select name from case_set').fetchall():
            flash('用例集名称不能重复', 'danger')
            return redirect(url_for('case_set'))
    except:
        pass
    if len(g.db.execute('select * from tmp_case').fetchall()) == 0:
        flash('未选择任何用例模板，不能创建', 'danger')
        return redirect(url_for('case_set'))
    case_detail = g.db.execute('select name,case_num from tmp_case order by id').fetchall()
    case_num = 0
    for elem in case_detail:
        case_num += int(elem[1])
    rate = round(len(case_detail) / (len(os.listdir('../model')) - 2), 4) * 100
    cover_rate = str(100 if rate >= 100 else rate) + ' %'
    g.db.execute('insert into case_set (name,create_time,case_num,cover_rate,case_detail) values (?,?,?,?,?)', [
        request.form['cname'], time.strftime('%y%m%d %H:%M', time.localtime()), str(case_num), cover_rate,
                 str(case_detail)])
    g.db.execute('drop table if exists model_case;')
    g.db.execute('drop table if exists tmp_case;')
    g.db.commit()
    flash('新建用例集成功', 'success')
    return redirect(url_for('case_set'))


# 用例集操作
@app.route('/case_set_operate', methods=['POST'])
def case_set_operate():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.form['key'] == '删除':
        if (request.form['name'],) in g.db.execute('select case_set from tasks').fetchall():
            flash('当前已有任务使用该用例集，请先删除任务', 'danger')
            return redirect(url_for('case_set'))
        g.db.execute('delete from case_set where name=(?)', [request.form['name']])
        g.db.commit()
        flash('删除用例集成功', 'success')
        return redirect(url_for('case_set'))
    else:
        set_detail = g.db.execute('select * from case_set where name=(?)', [request.form['name']]).fetchall()
        return str(set_detail)


# 自动化任务操作
@app.route('/task_operate', methods=['POST'])
def task_operate():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    global handle
    task_name = str(request.form['name'])
    if request.form['key'] == '启动':
        try:
            g.db.execute('drop table if exists "%s";' % task_name)
            g.db.commit()
            shutil.rmtree('../log/%s' % task_name)
            shutil.rmtree('../data/%s' % task_name)
        except:
            pass

        os.makedirs('../log/%s/error/image/' % task_name)
        os.makedirs('../data/%s/' % task_name)
        g.db.execute('update tasks set status="运行中",operate_time=(?),pass_num=0,pass_rate="0%" where name=(?)',
                     [time.strftime('%y%m%d %H:%M', time.localtime()), task_name])
        g.db.execute('create table "%s" (id integer primary key autoincrement,case_name string not null,\
                    case_page string,flag string,step_num string,type string,ordd string,\
                    xpath string, operate string,data string,step_flag string,img string);' % task_name)
        g.db.commit()
        #proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        s = socket.socket()
        s.connect(('127.0.0.1',1111))
        s.send(('task_name:%s' % task_name).encode('utf-8'))
        handle[task_name] = s
        print(handle[task_name])

    elif request.form['key'] == '删除':
        if g.db.execute('select status from tasks where'
                        ' name=(?)', [task_name]).fetchall()[0][0] not in ('已停止', '未执行', '已完成'):
            flash('请先停止任务后再执行删除操作', 'danger')
            return redirect(url_for('show_tasks'))
        else:
            try:
                g.db.execute('drop table if exists "%s";' % task_name)
                g.db.execute('delete from tasks where name=(?)', [task_name])
                g.db.commit()
                shutil.rmtree('../log/%s' % task_name)
                shutil.rmtree('../data/%s' % task_name)
            except:
                pass

    elif request.form['key'] == '详情':
        if g.db.execute('select status from tasks where'
                        ' name=(?)', [task_name]).fetchall()[0][0] == '未执行':
            flash('任务未启动，暂无详情信息', 'danger')
            return redirect(url_for('show_tasks'))
        if int(g.db.execute('select progress from tasks where name=(?)',
                            [task_name]).fetchall()[0][0].split('%')[0].split('.')[0]) < 10:
            flash('用例动态生成中...，暂无法查看详情', 'warning')
            return redirect(url_for('show_tasks'))
        case_detail = g.db.execute('select * from "%s" where type="0" order by id' % task_name).fetchall()
        step_detail = {}
        for elem in case_detail:
            tmp = g.db.execute('select * from "%s" where type="1" and case_name="%s" order by ordd'
                               % (task_name, elem[1])).fetchall()
            step_detail[elem[1]] = tmp

        return render_template('task_detail.html', cases=case_detail, steps=step_detail)

    elif request.form['key'] == '停止':
        handle[task_name].send(b'exit')
        handle[task_name].close()
        del handle[task_name]
        g.db.execute('update tasks set status="已停止" where name=(?)', [task_name])
        g.db.commit()
    return redirect(url_for('show_tasks'))


# 页面抽象编写
@app.route('/page_ab', methods=['POST', 'GET'])
def page_ab():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        page = request.form['page']
        root = ET.parse('../page/' + page + '.xml').getroot()
        page_para = {}
        xml_parse(root, page_para)
        return jsonify(page_para=page_para)
    else:
        pages = [elem.replace('.xml', '') for elem in os.listdir('../page/')]
        return render_template('page_ab.html', pages=pages)


# 页面抽象修改新增后下发
@app.route('/modify_page', methods=['POST'])
def modify_page():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    write_xml(request.form['page'], (request.form['add_row'], request.form['del_row'], request.form['modify']))
    return jsonify(code=200)


# 模板修改新增后下发
@app.route('/modify_model', methods=['POST'])
def modify_model():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    write_xml(request.form['model'], (request.form['add_row'], request.form['modify'], request.form['del_row']), flag=0)
    return jsonify(code=200)


# 新增抽象页面
@app.route('/xml_add', methods=['POST'])
def xml_add():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    obj = [elem.replace('.xml', '') for elem in os.listdir('../%s/' % request.form['para2'])]
    if request.form['para1'] in obj:
        code = 201
        msg = '名称重复'
    elif request.form['para1'] == '':
        code = 201
        msg = '名称不能为空'
    else:
        code = 200
        msg = ''
        with open('../%s/' % request.form['para2'] + request.form['para1'] + '.xml', 'w') as f:
            f.write('<?xml version="1.0"?><root></root>')
    return jsonify(code=code, msg=msg)


# 模板编写
@app.route('/model', methods=['POST', 'GET'])
def model():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        model = request.form['model']
        root = ET.parse('../model/' + model + '.xml').getroot()
        model_para = {}
        xml_parse(root, model_para, flag=0)
        return jsonify(model_para=model_para)
    else:
        models = [elem.replace('.xml', '') for elem in os.listdir('../model/')]
        return render_template('model.html', models=models)


@app.route('/get_xml', methods=['POST'])
def get_xml():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        para1 = request.form['para1']
        para2 = request.form['para2']
        if para2 == '2':
            root = ET.parse('../page/' + para1).getroot().find('html')
            module = [child.tag for child in root.getchildren()]
            return jsonify(module=module)
        elif para2 == '3':
            para3 = request.form['para3']
            root = ET.parse('../page/' + para1).getroot().find('html').find(para3)
            ty = [child.tag for child in root.getchildren()]
            s_ty = []
            for i in ty:
                s_ty.extend([i + '.' + child.tag for child in root.find(i).getchildren()])
            return jsonify(module=ty+s_ty)
        elif para2 == '5':
            return jsonify(module=['click', 'input', 'assert', 'getinfo', 'tri'])


@app.route('/bug_img')
def bug_img():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    img_path = request.args.get('p')
    print(img_path)
    with open(img_path, 'rb') as f:
        image = f.readlines()
    resp = Response(image, mimetype="image/png")
    return resp

@app.route('/api_record')
def api_record():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('api_record.html')


@app.route('/api_test', methods=['POST'])
def api_test():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    # 获取post传递过来的参数
    project_name = request.form['project']
    try:
        req_host = request.form['host']
        req_url = 'http://' + req_host + request.form['url']
        req_method = request.form['method']
    except:
        api_name = request.form['name']
        req_host  = g.db.execute('select host from project where name="%s";' % project_name).fetchall()[0][0]
        req_method, req_url = g.db.execute('select method, url from api where name="%s" and project_name="%s";' % (api_name, project_name)).fetchall()[0]
        req_url = 'http://' + req_host + req_url
    try:
        req_data = json.loads(request.form['data'])
    except:
        req_data = {}
    
    # 关键字替换变量
    Interface.dynamic_params(req_data)
    
    # 授权的处理
    req_auth = request.form['auth']
    
    # 头部处理
    if request.form['headers'] == '""':
        req_headers = {}
    else:
        req_headers = json.loads(request.form['headers'])
   
    # 刷新cookie
    Interface.host = req_host.split(':')[0]
    user_passwd = g.db.execute('select user_passwd from project where name="%s"' % project_name).fetchall()[0][0]
    if user_passwd:
        user_passwd = json.loads(user_passwd)
    try:
        r = set_cookie('公共-用户-用户登录', project_name, user_passwd)
        #print('cookie设置成功',project_name,r,Interface.cookie)
    except:
        #print('cookie设置失败',project_name,r,Interface.cookie)
        pass
    req_headers['Cookie'] = Interface.cookie
    
    # url中{}的参数替换
    if '{' in req_url:
        tmp = req_url.split('{')
        #print(tmp)
        for i in range(1, len(tmp)):
            tmp_key = tmp[i].split('}')[0]
            req_url = req_url.replace('{%s}' % tmp_key, req_data[tmp_key])
            del req_data[tmp_key]
    #print(req_url)
    
    # 进行请求
    try:
        if req_method == 'GET':
            if req_auth == '"none"':
                t = time.time()
                req = requests.get(req_url, params=req_data, headers=req_headers)
                print('\n', '[GET]', req.url)
                delt_t = str(round((time.time() - t)*1000, 1)) + ' ms'
            else:
                req_auth = json.loads(req_auth)
                if req_auth['auth_method'] == 'Basic':
                    t = time.time()
                    req = requests.get(req_url, params=req_data, headers=req_headers, auth=HTTPBasicAuth(req_auth['username'], req_auth['password']))
                    delt_t = str(round((time.time() - t)*1000, 1)) + ' ms'
                elif req_auth['auth_method'] == 'Digst':
                    t = time.time()
                    req = requests.get(req_url,params=req_data, headers=req_headers, auth=HTTPDigestAuth(req_auth['username'], req_auth['password']))
                    delt_t = str(round((time.time() - t)*1000, 1)) + ' ms'
        elif req_method == 'POST':
            if req_auth == '"none"':
                files = {}
                for key in req_data:
                    if isinstance(req_data[key], str):
                        if '*file.' in req_data[key]:
                            tmp = req_data[key].replace('*file.', '')
                            files[key] = (str(uuid.uuid1())+tmp.split('.')[-1], open('image/'+tmp, 'rb'))
                for key in files:
                    del req_data[key]
                t = time.time()
                if files != {}:
                    req = requests.post(req_url, params=req_data, files=files, headers=req_headers)   
                else:
                    req = requests.post(req_url, json=req_data, headers=req_headers)
                print('\n', '[POST]', req.url, req_data)
                delt_t = str(round((time.time() - t)*1000, 1)) + ' ms'
            else:
                req_auth = json.loads(req_auth)
                if req_auth['auth_method'] == 'Basic':
                    t = time.time()
                    req = requests.post(req_url, json=req_data, headers=req_headers, auth=HTTPBasicAuth(req_auth['username'], req_auth['password']))
                    delt_t = str(round((time.time() - t)*1000, 1)) + ' ms'
                elif req_auth['auth_method'] == 'Digst':
                    t = time.time()
                    req = requests.post(req_url, json=req_data, headers=req_headers, auth=HTTPDigestAuth(req_auth['username'], req_auth['password']))
                    delt_t = str(round((time.time() - t)*1000, 1)) + ' ms'
        elif req_method == 'PUT':
            if req_auth == '"none"':
                t = time.time()
                req = requests.put(req_url, json=req_data, headers=req_headers)
                delt_t = str(round((time.time() - t)*1000, 1)) + ' ms'
            else:
                req_auth = json.loads(req_auth)
                if req_auth['auth_method'] == 'Basic':
                    t = time.time()
                    req = requests.put(req_url, json=req_data, headers=req_headers, auth=HTTPBasicAuth(req_auth['username'], req_auth['password']))
                    delt_t = str(round((time.time() - t)*1000, 1)) + ' ms'
                elif req_auth['auth_method'] == 'Digst':
                    t = time.time()
                    req = requests.put(req_url, json=req_data, headers=req_headers, auth=HTTPDigestAuth(req_auth['username'], req_auth['password']))
                    delt_t = str(round((time.time() - t)*1000, 1)) + ' ms'
        elif req_method == 'DELETE':
            if req_auth == '"none"':
                t = time.time()
                req = requests.delete(req_url, headers=req_headers)
                delt_t = str(round((time.time() - t)*1000, 1)) + ' ms'
            else:
                req_auth = json.loads(req_auth)
                if req_auth['auth_method'] == 'Basic':
                    t = time.time()
                    req = requests.delete(req_url, headers=req_headers, auth=HTTPBasicAuth(req_auth['username'], req_auth['password']))
                    delt_t = str(round((time.time() - t)*1000, 1)) + ' ms'
                elif req_auth['auth_method'] == 'Digst':
                    t = time.time()
                    req = requests.delete(req_url, headers=req_headers, auth=HTTPDigestAuth(req_auth['username'], req_auth['password']))
                    delt_t = str(round((time.time() - t)*1000, 1)) + ' ms'
        
        # 响应处理
        res_headers = dict(req.headers)
        res_status_code = req.status_code
        try:
            res_data = req.json()
        except:
            res_data = str(req.text)
        res_time = delt_t
        
    except Exception as e:
        print(repr(e))
        res_status_code = 500
        res_time = 0
        res_data = {}
        res_headers = {}
        
    return jsonify({'status_code': res_status_code, 'request_time': res_time, 'response': res_data, 'res_h': res_headers, 'request': req_data})


@app.route('/project_api', methods=['POST'])
def project_api():
    if request.form['get'] == 'project':
        project_list = g.db.execute('select * from project;').fetchall()
        return jsonify(project=project_list)
    elif request.form['get'] == 'api':
        if request.form['type'] == 'list':
            api_list = [elem[0] for elem in g.db.execute('select name from api where project_name="%s" order by name;' % request.form['project_name']).fetchall()]
            return jsonify(api_list=api_list)
        
        api_list = g.db.execute('select * from api where project_name="%s" order by name;' % request.form['project_name']).fetchall()
        tmp = {}
        for elem in api_list:
            k = elem[1].split('-')[0]
            v = elem[1].replace(k+'-', '')
            if k in tmp:
                tmp[k].append(v)
            else:
                tmp[k] = [v]
        return jsonify(api=tmp)
    elif request.form['get'] == 'single_api':
        api = g.db.execute('select * from api where name="%s";' % request.form['api_name']).fetchall()[0]
        return jsonify({'method':api[3], 'url':api[4], 'data':api[5], 'headers':api[6], 'auth':api[7], 'assert_data':api[8], 'host': api[9]})
    elif request.form['get'] == 'api_data':
        project = request.form['project_name']
        api = request.form['api_name']
        data = json.loads(g.db.execute('select data from api where name="%s" and project_name="%s";' % (api, project)).fetchall()[0][0])
        assert_data = json.loads(g.db.execute('select assert from api where name="%s" and project_name="%s";' % (api, project)).fetchall()[0][0])
        for key in assert_data:
            assert_data[key] = assert_data[key]['assert_value']
        return jsonify(data=data, assert_data=assert_data)
    elif request.form['get'] == 'del':
        try:
            g.db.execute('delete from api where name="%s" and project_name="%s";' % (request.form['api_name'], request.form['project_name']))
            g.db.commit()
            return jsonify(msg='删除成功')
        except Exception as e:
            return jsonify(msg='删除失败'+repr(e))
        
        
@app.route('/api_save', methods=['POST'])
def api_save():
    flag = request.form['flag']
    req_host = request.form['host']
    req_api_name = request.form['api_name']
    req_project_name = request.form['project_name']
    req_url = request.form['url']
    req_method = request.form['method']
    req_data = request.form['data'] 
    req_auth = request.form['auth']
    req_headers = request.form['headers']
    req_assert_data = request.form['assert_data']
    
    # 新增api
    if flag == '1':
        obj = g.db.execute("select * from api where name='%s' and project_name='%s';" % (req_api_name, req_project_name)).fetchall()
        if len(obj):
            return jsonify(code=500, msg='接口重名')
        try:
            g.db.execute("insert into api (name, project_name, method, url, data, headers, auth, assert, host) values('%s','%s', '%s', '%s', '%s','%s', '%s', '%s', '%s');" % (req_api_name, req_project_name, req_method, req_url, req_data, req_headers, req_auth, req_assert_data, req_host))
            g.db.commit()
            return jsonify(code=200)
        except Exception as msg:
            return jsonify(code=500, msg=msg)
    # 修改api
    else:
        obj = g.db.execute("select * from api where name='%s' and project_name='%s';" % (req_api_name, req_project_name)).fetchall()
        if not len(obj):
            return jsonify(code=500, msg='接口不存在，无法修改')
        try:
            g.db.execute("update api set method='%s', url='%s', data='%s', headers='%s', auth='%s', assert='%s', host='%s' where name='%s' and project_name='%s';" % (req_method, req_url, req_data, req_headers, req_auth, req_assert_data, req_host, req_api_name, req_project_name))
            g.db.commit()
            return jsonify(code=200)
        except Exception as msg:
            return jsonify(code=500, msg=msg)


@app.route('/interf_scene', methods=['GET', 'POST'])
def interf_scene():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'GET':
        project = [elem[0] for elem in g.db.execute('select name from project;').fetchall()]
        return render_template('interf_scene.html', projects=project)
    elif request.method == 'POST':
        project = request.form['project']
        if request.form['type'] == 'get_scene_data':
            scene = request.form['scene']
            data = g.db.execute('select data from scene where name="%s" and project="%s";' % (scene, project)).fetchall()[0][0]
            if data is None:
                return jsonify(cases=[])
            else:
                data = data.split(',')
            s_key = g.db.execute('select id from scene where name="%s" and project="%s";' % (scene, project)).fetchall()[0][0]
            cases = []
            for k,v in enumerate(data):
                cases.append(g.db.execute('select name,data,assert_data,save_data,del_data,pre_time from "case" where name="%s" and s_key="%s"' % (v, s_key)).fetchall()[data[:k].count(v)])
            return jsonify(cases=cases)
        elif request.form['type'] == 'new':
            if (request.form['name'],) in g.db.execute('select name from scene where project="%s";' % (request.form['project'])).fetchall():
                return jsonify(code=201, message='场景名重复！')
            else:
                g.db.execute('insert into scene (name, project) values("%s", "%s");' % (request.form['name'], request.form['project']))
                g.db.commit()
                return jsonify(code=200, message='场景新建成功，请补充用例！')
        elif request.form['type'] == 'modify':
            api_list = json.loads(request.form['data'])
            api_data = json.loads(request.form['case_data'])
            name = request.form['scene']
            Scene.modify([project, name, api_list], api_data)
            return jsonify(code=200, message='场景《%s》修改成功' % name)
        elif request.form['type'] == 'del_scene':
            try:
                # 删除场景
                g.db.execute('delete from scene where project="%s" and name="%s"' % (request.form['project'], request.form['scene']))
                # 删除测试套中包含的该场景
                for elem in g.db.execute('select id,data from suite where project="%s";' % request.form['project']).fetchall():
                    if elem[1] is None:
                        continue
                    if request.form['scene'] in elem[1]:
                        g.db.execute('update suite set data="%s" where id=%d;' % (elem[1].replace(request.form['scene']+',', '').replace(request.form['scene'], ''), elem[0]))
                g.db.commit()
                return jsonify(message='删除成功')
            except Exception as e:
                return jsonify(message='删除失败'+e)
        scene = [elem[0] for elem in g.db.execute('select name from scene where project="%s";' % project).fetchall()]
        return jsonify(scene=scene)
    

@app.route('/suite', methods=['GET', 'POST'])
def suite():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'GET':
        project = [elem[0] for elem in g.db.execute('select name from project;').fetchall()]
        return render_template('suite.html', projects=project)
    elif request.method == 'POST':
        if request.form['type'] == 'get_suite':
            suite = [elem[0] for elem in g.db.execute('select name from suite where project="%s";' % request.form['project']).fetchall()]
            return jsonify(suite=suite)
        elif request.form['type'] == 'get_scene':
            all_scene = [elem[0] for elem in g.db.execute('select name from scene where project="%s";' % request.form['project']).fetchall()]
            scene = g.db.execute('select data from suite where name="%s"' % request.form['suite']).fetchall()[0][0]
            if scene is None or scene=='':
                scene = []
            else:
                scene = scene.split(',')
            for i in scene:
                all_scene.remove(i)
            return jsonify(all_scene=all_scene, scene=scene)
        elif request.form['type'] == 'modify_suite':
            scene_data = ','.join(json.loads(request.form['data']))
            g.db.execute('update suite set data="%s" where name="%s" and project="%s"' % (scene_data, request.form['name'], request.form['project']))
            g.db.commit()
            return jsonify(code=200, message="测试套《%s》修改成功！" % request.form['name'])
        elif request.form['type'] == 'del_suite':
            try:
                if (request.form['suite'],) in g.db.execute('select suite from interf_task;').fetchall():
                    return jsonify(msg="删除失败，测试套已被加载到任务，请先删除任务后再执行该操作！")
                else:
                    g.db.execute('delete from suite where name="%s" and project="%s";' % (request.form['suite'], request.form['project']))
                    g.db.commit()
                    return jsonify(msg="删除成功")
            except Exception as e:
                return jsonify(msg="Error:"+repr(e))
        elif request.form['type'] == 'new_suite':
            try:
                if (request.form['suite'],) in g.db.execute('select name from suite;').fetchall():
                    return jsonify(msg="测试套名称重复，请重新输入！")
                else:
                    g.db.execute('insert into suite(name,project) values("%s","%s");' % (request.form['suite'], request.form['project']))
                    g.db.commit()
                    return jsonify(msg="新增测试套成功")
            except Exception as e:
                return jsonify(msg="Error:"+repr(e))
     
    
@app.route('/interf_task', methods=['GET', 'POST'])
def interf_task():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'GET':
        project = [elem[0] for elem in g.db.execute('select name from project;').fetchall()]
        return render_template('interf_task.html', projects=project)
    elif request.method == 'POST':
        if request.form['type'] == 'get_task':
            task = g.db.execute('select * from interf_task where project="%s" order by id desc' % request.form['project']).fetchall()
            return jsonify(task=task)
        elif request.form['type'] == 'new_task':
            task_name = request.form['name']
            project = request.form['project']
            suite = request.form['suite']
            if (task_name,) in g.db.execute('select name from interf_task where project="%s";' % project).fetchall():
                return jsonify(code=201, message="任务名称重复！")
            scene_num = len(g.db.execute('select data from suite where name="%s" and project="%s";' % (suite, project)).fetchall()[0][0].split(','))
            g.db.execute('insert into interf_task(name,suite,project,scene_num) values("%s","%s","%s","%d");' % (task_name,suite,project,scene_num))
            g.db.commit()
            return jsonify(code=200)
        elif request.form['type'] == 'del_task':
            try:
                log_file = json.loads(g.db.execute('select result from interf_task where name="%s" and project="%s";' %(request.form['name'], request.form['project'])).fetchall()[0][0])
                log_file_list = []
                for elem in log_file:
                    for i in elem[1]:
                        log_file_list.append(i[2])
            except:
                log_file_list = []
            g.db.execute('delete from interf_task where name="%s" and project="%s";' % (request.form['name'], request.form['project']))
            g.db.commit()
            # 删除任务日志
            for elem in log_file_list:
                try:
                    os.remove(elem)
                except:
                    pass
            
            return jsonify(code=200, message="任务删除成功！")
        # 启动任务
        elif request.form['type'] == 'start_task':
            # 同步测试套数量
            suite_name = g.db.execute('select suite from interf_task where name="%s" and project="%s";' %(request.form['name'], request.form['project'])).fetchall()[0][0]
            scene_num = len(g.db.execute('select data from suite where name="%s" and project="%s";' %(suite_name, request.form['project'])).fetchall()[0][0].split(','))
            try:
                log_file = json.loads(g.db.execute('select result from interf_task where name="%s" and project="%s";' %(request.form['name'], request.form['project'])).fetchall()[0][0])
                log_file_list = []
                for elem in log_file:
                    for i in elem[1]:
                        log_file_list.append(i[2])
            except:
                log_file_list = []
            
            # 初始化任务数据
            g.db.execute('update interf_task set run_time="%s",progress="0",scene_num=%s,pass_num=0,pass_rate="0",status=1,result="[]" where name="%s" and project="%s";' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),scene_num,request.form['name'],request.form['project']))
            g.db.commit()
                
            # 删掉之前的任务日志
            for elem in log_file_list:
                try:
                    os.remove(elem)
                except:
                    pass
            t = Task(request.form['name'],request.form['project'])
            t.run()
            return jsonify(code=200)
        
        
@socketio.on('connect', namespace='/task_i')
def push_task_i():
    with thread_lock:
        s = connect_db()
        conn_num = s.execute('select conn_num from push where namespace="/task_i"').fetchall()[0][0]+1
        conn_num = s.execute('update push set conn_num="%d" where namespace="/task_i"' % conn_num)
        s.commit()
        if not s.execute('select status from push where namespace="/task_i"').fetchall()[0][0]:
            s.execute('update push set status=1 where namespace="/task_i"')
            s.commit()
            t = Thread(target=refresh_task_i)
            t.start()
        s.close()
        
@socketio.on('disconnect', namespace='/task_i')
def del_conn():
    with thread_lock:
        s = connect_db()
        conn_num = s.execute('select conn_num from push where namespace="/task_i"').fetchall()[0][0]-1
        conn_num = s.execute('update push set conn_num="%d" where namespace="/task_i"' % conn_num)
        s.commit()
        s.close()
    
def refresh_task_i():
    s = connect_db()
    while True:
        time.sleep(6)
        with thread_lock:
            if s.execute('select conn_num from push where namespace="/task_i"').fetchall()[0][0] == 0:
                s.execute('update push set status=0 where namespace="/task_i"')
                s.commit()
                s.close()
                break
            else:
                socketio.emit('task_data', {'msg': 'ok'}, namespace='/task_i')
            
            
@app.route('/task_detail', methods=['GET'])
def task_detail():
    result = json.loads(g.db.execute('select result from interf_task where name="%s" and project="%s";' % (request.args['name'], request.args['project'])).fetchall()[0][0])
    return render_template('result.html', result=result)
            
            

@app.route('/interf_log', methods=['POST'])
def interf_log():
    try:
        with open(request.form['logfile'], 'r') as f:
            log_ = f.read()
    except:
        log_ = '日志未找到！'
    return jsonify(log=log_)


@app.route('/project_m', methods=['GET', 'POST'])
def project_m():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'GET':
        project = g.db.execute('select name,host,user_passwd from project;').fetchall()
        return render_template('project_m.html', projects=project)
    elif request.method == 'POST':
        project = request.form['project']
        if request.form['type'] == 'add':
            if (project,) in g.db.execute('select name from project;').fetchall():
                return jsonify({'code':201, 'msg':'项目名重复'})
            else:
                g.db.execute('insert into project (name) values("%s")' % project)
                g.db.commit()
                return jsonify(code=200)
        elif request.form['type'] == 'del':
            try:
                g.db.execute('delete from project where name="%s";' % project)
                g.db.commit()
                return jsonify(code=200)
            except Exception as e:
                return jsonify(code=201, msg=e)
        elif request.form['type'] == 'mod':
            try:
                g.db.execute("update project set host='%s',user_passwd='%s' where name='%s';" % (request.form['host'], request.form['user_passwd'], project))
                g.db.commit()
                return jsonify(code=200)
            except Exception as e:
                return jsonify(code=201, msg=repr(e))
