from tkinter import *
import tkinter.filedialog
import pymysql
import threading
import tkinter.messagebox  # 这个是消息框，对话框的关键
import logging

'''
数据库导入脚本，旧数据库往新数据库导入

注意：
批量导入sql语句，要求:
1、关键字必须大写
2、两个字段之间用逗号+空格（因使用MD5连接字符时，会有，程序中有通过逗号分隔字符串）比如openid tc002_openid, username tc002_user_name,
3、.txt文档，sql文末不能有空行
4、正式导入数据时，先查询有多少条数据，再导入。查询时的条数与导入时相同
5、文件编码格式必须是UTF-8
导入sql示例：phome_enewsmember 旧表，gt003_user_normal 新表
SELECT UUID() tc012_user_role_id, userid tc001_user_id, 'f1a243dc-4bbe-94c3-d707-d91f7bd5c18c' tc008_role_id FROM phome_enewsmember where groupid in(0,1);gt003_user_normal

'''

# import io
# import sys

# config = {
#     'host': '47.100.60.152',
#     'port': 3306,
#     'user': 'gttest',
#     'password': 'COk+Y5.g8FDxJ5s',
#     'db': 'ceshihao3.6',
#     'charset': 'utf8'
# }

config = {
    'host': 'rm-bp11g1br1u79795y5rw.mysql.rds.aliyuncs.com',
    'port': 3306,
    'user': 'zjk',
    'password': 'zjk940915++',
    'db': 'hao',
    'charset': 'utf8'
}

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
#
# config = {
#     'host': '192.168.1.27',
#     'port': 3306,
#     'user': 'root',
#     'password': '123456',
#     'db': 'beidi',
#     'charset': 'utf8'
# }



filename = ''
threadStatus = 'true'


# f = open('E:\桌面\log.txt', 'a', encoding='utf-8')
# line.decode("utf8","ignore")
def selectPath():
    global filename
    # filename = tkinter.filedialog.askopenfilename(filetypes = [('TXT', 'txt')])
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        path.set(filename)
    else:
        path.set("You did not select the file.")


def startInsertData():
    readfile(filename)


def stopThread():
    global threadStatus
    threadStatus = 'false'


def getItemName(sql):
    result = sql.split('FROM')[0].split('SELECT')[1].split(', ')  # 取出sql中需要截取的字符串
    print(result)
    field_name = []
    for item in result:
        field_name.append(item.rstrip().split(' ')[-1])  # 将取到的别名，增加到field_name列表中
    length = len(field_name)
    place = ('{}'.format('%s,') * length).rstrip(',')
    print(length)
    print(field_name)
    delimiter = ','
    field_name = delimiter.join(field_name)
    return [field_name, place]


def getTableName(sql):
    result = sql.split(';')[1]
    return result


def readfile(fileurl):
    print(fileurl)
    for line in open(fileurl, encoding='utf-8'):
        # print(line)
        if 'SELECT' in line:
            print(line)
            global threadStatus
            threading.Thread(target=insertDate, args=(
            getItemName(line)[0], getItemName(line)[1], getTableName(line), line.split(';')[0],)).start()



def showInfo(str):
    # global logger
    logger = logging.getLogger('log')
    logger.setLevel(level = logging.INFO)
    hanlder = logging.FileHandler('log.txt')
    hanlder.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    hanlder.setFormatter(formatter)
    logger.addHandler(hanlder)

    logger.info(str)
    # logger.removeHandler(hanlder)
    logger.handlers.pop()


def showErr(str):

    logger2 = logging.getLogger('log2')
    logger2.setLevel(level = logging.ERROR)
    hanld = logging.FileHandler('log.txt')
    hanld.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    hanld.setFormatter(formatter)
    logger2.addHandler(hanld)

    logger2.error(str)
    # logger2.removeHandler(hanld)
    logger2.handlers.pop()


def insertDate(field_name, place, table, sql):
    if threadStatus == 'false':
        print(table + 'Stop success')
        return
    conn = pymysql.connect(**config)  # 注意传入的数据为字典类型
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    j = 0
    k = len(data)
    print(k, place, sql)
    for items in data:
        if type(items) == tuple:
            len(items)
            # print(items)
            try:
                i = 'insert into ' + table + '(' + field_name + ') values(' + place + ')'
                cur.execute(i, items)
                print(items)
                print('\n')
                print(i)
                print('\n')
                conn.commit()
            except Exception as err:
                print(err)
                conn.rollback()
                showErr(err)
                # threading.Thread(target=showErr, args=err,).start()
            j += 1
            print(j)
            print('\n')
    # nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print((nowTime + table+'Finish ' +  'selcet:%d'%k +  '\000' + ' insert:%d'%j), file = f)
    select_info = str( table + ' finish ' + ' selcet:%d' % k + ' insert:%d' % j)
    showInfo(select_info)
    conn.close()


root = Tk()
path = StringVar()

Label(root, text="target path:").grid(row=0, column=0)
Entry(root, textvariable=path).grid(row=0, column=1)
Button(root, text="path choice", command=selectPath).grid(row=0, column=2)

Button(root, text="Start run", command=startInsertData).grid(row=1, column=1)
Button(root, text="Stop run", command=stopThread).grid(row=1, column=2)

if __name__ == '__main__':
    root.mainloop()


