# coding:utf-8
'''
接口类：实现接口参数化操作
支持：
    1、环境参数修改（Interface类变量）；
    2、post/get下发参数修改（Interface实例变量self.params）
    3、接口响应后，响应参数校验（Interface实例变量
        self.result <三方库requests中的Response对象>）
    4、响应参数保存/删除，保存到self.g这个线程局部变量中
        （方便多个接口请求时，中间数据传递）
    5、下发参数self.params动态替换（self.g这个线程局部变量,
        以及时间参数
        （'*now', '*today0', '*today24', '*now+x', '*now-x'））
'''

__all__ = ['Interface', 'set_cookie', 'interf']


import json
import requests
import time
import sqlite3
import base64
import random
import os
import uuid
import logging
import traceback


class Interface:
    '''
    接口类，通过http请求方法，url，请求参数来实例化。
    支持时间参数动态生成 _dynamic_params
    方法request可进行接口调用（必须参数HOST，可选参数Cookie）
    
    '''
    
    # 类变量
    host = ''
    db_path = 'web.db'
    cookie = None
    protocol = 'http://'# https://
    
    # 实例化方法
    def __init__(self, method, url, params, headers=None, g={}, log=True):
        # 基本属性
        if log:
            self.log_file = 'log/'+str(uuid.uuid1())+'_'+str(int(time.time()*1000))+'_log.txt'
        else:
            self.log_file = None
        self.method = method
        self.url = url
        self.params = params
        self.headers = headers if headers else {}
        
        # 下发参数的key
        self.params_key = (key for key in self.params)
        
        # 下发参数动态处理
        Interface.dynamic_params(self.params)
        
        # 接口下发后，响应结果对象
        self.result = None
        self.g = g
        
    def log(self, msg, content):
        if self.log_file:
            with open(self.log_file, 'a+') as f:
                f.write('['+msg+']  '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+'\n'+content+'\n\n')

    # 参数修改
    def modify_params(self,k_v):
        if k_v == '' or k_v == None:
            k_v = {}
            return
        try:
            Interface.dynamic_params(k_v)
            self.g_replace(k_v)

        except:
            print(traceback.format_exc())
            self.log('info','Modify_params failed! '+str(k_v))
            
    # 下发接口
    def request(self):
        try:
            # url中{}的参数替换
            if '{' in self.url:
                tmp = self.url.split('{')
                for i in range(1, len(tmp)):
                    tmp_key = tmp[i].split('}')[0]
                    self.url = self.url.replace('{%s}' % tmp_key, self.params[tmp_key])
                    del self.params[tmp_key]

            if Interface.cookie:
                self.headers['Cookie'] = Interface.cookie  
            if self.method == 'GET':
                r = requests.request(self.method, Interface.protocol+Interface.host+self.url, 
                            params=self.params, headers=self.headers)
            elif self.method == 'DELETE':
 
                r = requests.request(self.method, Interface.protocol+Interface.host+self.url, headers=self.headers)
            elif self.method == 'POST' or self.method == 'PUT':
                files = {}
                for key in self.params:
                    if isinstance(self.params[key], str):
                        if '*file.' in self.params[key]:
                            tmp = self.params[key].replace('*file.', '')
                            files[key] = (str(uuid.uuid1())+tmp.split('.')[-1], open('image/'+tmp, 'rb'))
                for key in files:
                    del self.params[key]
                if files:
                    r = requests.request(self.method, Interface.protocol+Interface.host+self.url, 
                            params=self.params, files=files, headers=self.headers)
                else:
                    r = requests.request(self.method, Interface.protocol+Interface.host+self.url, 
                            json=self.params, headers=self.headers)
            self.result = r
            self.log('info','Interface %s requested success!' % self.url)
            self.log('info','Interface %s request and response info:' % self.url+'\n'+
                    '请求:'+'\n'+'*'*60+'\n'+self.method+'  '+Interface.host+' '+self.url+'\n'+
                    '头部\n'+str(self.result.request.headers)+'\n参数\n'+str(self.params)+'\n'+
                    '响应:   '+str(self.result.status_code)+'\n'+'*'*60+'\n'+
                    '头部\n'+str(self.result.headers)+'\n'+'参数\n'+str(self.result.json()))
            return True
        except Exception as e:
            self.result = None
            self.log('error','Interface %s requested failed!' % self.url + '\n' + str(e))
            self.log('info','Interface %s request and response info:' % self.url+'\n'+
                    '请求:'+'\n'+'*'*60+'\n'+self.method+'  '+Interface.host+' '+self.url+'\n'+'头部\n'+
                    str(self.headers)+'\n'+'参数\n'+str(self.params))
            return False
        
    # 响应结果校验
    def assert_response(self, k_v):
        if self.result == None:
            self.log('info','Request failed. Assert operation is invailed!')
            return False
 
        self.g_replace(k_v)
        for k in k_v:
            try:
                if k == 'status_code':
                    obj = self.result.status_code
                    o_obj = int(k_v[k])
                elif 'headers.' in k:
                    obj = self.result.headers[k.split('.')[1]]
                    o_obj = k_v[k]
                else:
                    
                    obj = self.get_json(k)
                    o_obj = k_v[k]
                assert(str(obj) == str(o_obj))
                self.log('info','Assert success!  '
                            +k+': '+str(o_obj)+' | '+str(obj))
            except:
                #print(traceback.format_exc())
                self.log('error','Assert failed!  '
                             +k+' : '+str(o_obj)+' | '+str(obj))
                return False
        return True
    
    # 响应结果json数据获取
    def get_json(self, key):
        try:
            tmp = self.result.json()
        except:
            print(traceback.format_exc())
            return None
            self.log('error','Get_json! '+ str(self.result.content))
        try:
            for elem in key.split('.'):
                if elem == '*r':
                    tmp = random.sample(tmp,1)[0]
                else:
                    if elem.isdigit():
                        elem = int(elem)
                    tmp = tmp[elem]
            return tmp
        except:
            print(traceback.format_exc())
            return None
        
    
    # 保存过程值
    def g_push(self, key_list):
        # print(self.g)
        try:
            for k in key_list:
                if k in self.g:
                    if k+'0' not in self.g:
                        self.g[k+'0'] = 1
                        self.g[k+'1'] = self.g[k]
                    if isinstance(self.get_json(k), dict) or isinstance(self.get_json(k), list):
                        self.g[k+str(self.g[k+'0']+1)] = json.dumps(self.get_json(k))
                    else:
                        self.g[k+str(self.g[k+'0']+1)] = self.get_json(k)
                    self.log('info','G push values: ' + str(k)+':' + str(self.g[k+str(self.g[k+'0']+1)]))
                    self.g[k+'0'] = self.g[k+'0'] + 1
                else:
                    if isinstance(self.get_json(k), dict) or isinstance(self.get_json(k), list):
                        self.g[k] = json.dumps(self.get_json(k))
                    else:
                        self.g[k] = self.get_json(k)
                    self.log('info','G push values: ' + str(k)+':'+str(self.g[k]))
                    # self.log('info',str(self.g))
        except:
            print(traceback.format_exc())
            self.log('error','G_push failed! '+ str(key_list) + '  ' + str(self.g))
          
        
    # 全局参数替换
    def g_replace(self, k_v):
        try:
            for k in k_v:
                if isinstance(k_v[k], list):
                    for i in range(len(k_v[k])):
                        if isinstance(k_v[k][i],dict):
                            self.g_replace(k_v[k][i])
                elif isinstance(k_v[k], dict):
                    self.g_replace(k_v[k])
                elif isinstance(k_v[k], str):
                    if '*g.' in k_v[k]:
                        # print(k, k_v[k], '*'*10,'\n')
                        tmp_v = []
                        for elem in k_v[k].split(','):
                            if '..' in elem:
                                tmp = self.g[elem.split('..')[0].replace('*g.', '')]
                                for child in elem.split('..')[1].split('.'):
                                    try:
                                        tmp = tmp[int(child)]
                                    except:
                                        print(traceback.format_exc())
                                        tmp = tmp[child]
                                try:
                                    tmp_v.append(json.loads(tmp))
                                except:
                                    tmp_v.append(tmp)
                            else:
                                try:
                                    tmp_v.append(json.loads(self.g[elem.replace('*g.', '')]))
                                except:
                                    tmp_v.append(self.g[elem.replace('*g.', '')])
                        if len(tmp_v) > 1:
                            k_v[k] = ','.join([str(elem) for elem in tmp_v])
                        else:
                            try:
                                k_v[k] = json.loads(tmp_v[0])
                            except:
                                k_v[k] = tmp_v[0]
  
        except:
            print(traceback.format_exc())
            self.log('error','G_replace failed! '+ str(k_v))

    # 特殊参数动态生成（主要是时间类）
    @staticmethod
    def dynamic_params(params):
        for key in params:
            #print(key)
            if not isinstance(params[key], str):
                if isinstance(params[key], list):
                    for i in range(len(params[key])):
                        if isinstance(params[key][i],dict):
                            Interface.dynamic_params(params[key][i])
                elif isinstance(params[key], dict):
                    Interface.dynamic_params(params[key])
                else:
                    continue

            if params[key] == '*now':
                params[key] = int(time.time()*1000)
            elif params[key] == '*today0':
                current_time = time.time()
                params[key] = int((current_time-current_time%86400-8*3600
                                         )*1000)
            elif params[key] == '*today24':
                current_time = time.time()
                params[key] = int((current_time-current_time%86400-8*3600
                                         +24*3600)*1000-1)
            elif '*now+' in params[key]:
                interval = int(float(params[key].split('+')[1])*3600*1000)
                params[key] = int(time.time()*1000) + interval 
            elif '*now-' in params[key]:
                interval = int(float(params[key].split('-')[1])*3600*1000)
                params[key] = int(time.time()*1000) - interval
            elif '*base64.' in params[key]:
                params[key] = img_b64(os.getcwd() + '/image/'+ params[key].replace('*base64.', ''))
            elif params[key] == 'true':
                params[key] = True
            elif params[key] == 'false':
                params[key] = False


# 登陆获取cookie，并保存到Interfa的类变量中
def set_cookie(interface_name, project, data=None):
    i = interf(interface_name, project, g={}, log=False)
    if data:
        i.modify_params(data)
    i.request()
    Interface.cookie = i.result.headers['Set-Cookie'].split(';')[0]
    return i.result.json()
    

# 从数据库api表中读取接口参数，并实例化对象
def interf(interface_name, project, g={}, log=True):
    db = sqlite3.connect(Interface.db_path)
    result = db.execute('select method,url,data'
                  ' from api where project_name="%s" and name="%s"'
                  % (project, interface_name))
    tmp = list(result.fetchall()[0])
    tmp[2] = json.loads(tmp[2])
    return Interface(*tmp, g=g, log=log)


# 图片base64编码
def img_b64(img_path):
    try:
        with open(img_path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    except:
        return img_path+'未找到图片'
    
