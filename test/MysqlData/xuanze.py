from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter.filedialog
import pymysql
import threading
import tkinter.messagebox #这个是消息框，对话框的关键

# config = {
#     'host': '47.100.60.152',
#     'port': 3306,
#     'user': 'gttest',
#     'password': 'COk+Y5.g8FDxJ5s',
#     'db': 'ceshihao3.6',
#     'charset': 'utf8'
# }

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
        path.set("You did not select the file.")
		
def startInsertData():
    readfile(filename)
	
def stopThread():
    global threadStatus
    threadStatus='false'
	
def getItemName(sql):
    result = sql.split('FROM')[0].split('SELECT')[1].split(', ')  # 取出sql中需要截取的字符串
    print(result)
    field_name = []
    for item in result:
        field_name.append(item.rstrip().split(' ')[-1]) # 将取到的别名，增加到field_name列表中
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
    for line in open(fileurl,encoding='UTF-8'):  
        print(line)
        global threadStatus
        threading.Thread(target=insertDate,args=(getItemName(line)[0],getItemName(line)[1],getTableName(line),line.split(';')[0],)).start()

def showErr(str):
    tkinter.messagebox.showerror('Report error',str)
	
		
def insertDate(field_name, place,table,sql):
        if threadStatus == 'false':
            print(table+'Stop success')
            return
        conn = pymysql.connect(**config) # 注意传入的数据为字典类型
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        j=0
        k=len(data)
        print(k,place,sql)
        for items in data:
            if type(items) == tuple:
                len(items)
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
                    print(err)
                    conn.rollback()
                    threading.Thread(target=showErr,args=(err,)).start()
                j += 1
        conn.close()
        print(table+'Finish ' +  'selcet:%d'%k + ' insert:%d'%j)
        tkinter.messagebox.showinfo('info', table + 'finish'  + 'selcet:%d'%k + ' insert:%d'%j)

root = Tk()
path = StringVar()

Label(root,text = "target path:").grid(row = 0, column = 0)
Entry(root, textvariable = path).grid(row = 0, column = 1)
Button(root, text = "path choice", command = selectPath).grid(row = 0, column = 2)

Button(root, text = "Start run", command = startInsertData).grid(row = 1, column = 1)
Button(root, text = "Stop run", command = stopThread).grid(row = 1, column = 2)

root.mainloop()
