from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter.filedialog
import pymysql
import threading
import tkinter.messagebox #这个是消息框，对话框的关键

config = {
    'host': '192.168.1.27',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'beidi',
    'charset': 'utf8'
}
	
filename=''
threadStatus='true'

def selectPath():
    global filename
    filename = tkinter.filedialog.askopenfilename(filetypes = [('TXT', 'txt')])
    if filename != '':
        path.set(filename)
    else:
        path.set("您没有选择任何文件")
		
def startInsertData():
    readfile(filename)
	
def stopThread():
    global threadStatus
    threadStatus='false'
	
def getItemName(sql):
    result = sql.split('FROM')[0].split('SELECT')[1].split(',')  # 取出sql中需要截取的字符串
    #print(result)
    field_name = []
    for item in result:
        field_name.append(item.rstrip().split(' ')[-1]) # 将取到的别名，增加到field_name列表中
    length = len(field_name)
    place = ('{}'.format('%s,') * length).rstrip(',')
    # print(length)
    delimiter = ','
    field_name = delimiter.join(field_name)
    return [field_name, place]		

def getTableName(sql):
    result = sql.split(';')[1]
    return result
	
def readfile(fileurl):
    for line in open(fileurl,encoding='UTF-8'):  
        print(line)
        global threadStatus
        threading.Thread(target=insertDate,args=(getItemName(line)[0],getItemName(line)[1],getTableName(line),line.split(';')[0],)).start()

def showErr(str):
    tkinter.messagebox.showerror('报错',str)
	
		
def insertDate(field_name, place,table,sql):
        if threadStatus == 'false':
            print(table+'停止成功')
            return;
        conn = pymysql.connect(**config) # 注意传入的数据为字典类型
			
        # conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='beidi', charset='utf8')
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()

        for items in data:
            if type(items) == tuple:
                # print(items)
                try:
                    i = 'insert into '+table+'('+field_name+') values('+place+')'
                    cur.execute(i, items)
                    print(items)
                    print('\n')
                    print(i)
                    print('\n')
                    conn.commit()
                except Exception as err:
                    #print(err)
                    conn.rollback()
                    threading.Thread(target=showErr,args=(err,)).start()

        conn.close()
        print(table+'插入完成')
        tkinter.messagebox.showinfo('提示',table+'插入完成')

root = Tk()
path = StringVar()

Label(root,text = "目标路径:").grid(row = 0, column = 0)
Entry(root, textvariable = path).grid(row = 0, column = 1)
Button(root, text = "路径选择", command = selectPath).grid(row = 0, column = 2)

Button(root, text = "开始执行", command = startInsertData).grid(row = 1, column = 1)
Button(root, text = "停止执行", command = stopThread).grid(row = 1, column = 2)

root.mainloop()

