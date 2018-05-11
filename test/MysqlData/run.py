"""
@Name: jk
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/5/3
"""

# <span style="font-size:24px;"> #简单的图形界面GUI（Graphical User Interface）
from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter.filedialog
import pymysql
import threading
import tkinter.messagebox

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


class Application(Frame):   #从Frame派生出Application类，它是所有widget的父容器
    def __init__(self,master = None):#master即是窗口管理器，用于管理窗口部件，如按钮标签等，顶级窗口master是None，即自己管理自己
        Frame.__init__(self,master)
        self.quitButton = Button(self,text = 'quit',command = self.quit)#创建一个Quit按钮，实现点击即退出窗口
        self.nameButton = Button(self,text = 'hello',command = self.run)#创建一个hello按钮，点击调用hello方法，实现输出
        # self.pathButton = Button(self,text = 'open file',command = self.selectPath)#创建一个hello按钮，点击调用hello方法，实现输出
        self.pack()#将widget加入到父容器中并实现布局
        self.createWidgets()

    def createWidgets(self):
        self.field_name = Label(self,text = 'input field_name')#创建一个标签显示内容到窗口
        self.field_name.pack()

        self.input_field_name = Entry(self)#创建一个输入框，以输入内容
        self.input_field_name.pack()

        self.sql = Label(self, text='input sql')  # 创建一个标签显示内容到窗口
        self.sql.pack()

        self.input_sql = Entry(self)  # 创建一个输入框，以输入内容
        self.input_sql.pack()

        self.nameButton = Button(self, text='run', command=self.run)
        self.nameButton.pack()

        self.quitButton.pack()

    def run(self):
        field_name = self.input_field_name.get()#获取输入的内容
        value = self.getItemName(field_name)
        sql = self.input_sql.get()
        self.insertDate(value[0], value[1], sql, )


if __name__ == '__main__':

    app = Application()
    app.master.title("mysql")#窗口标题
    app.mainloop()#主消息循环</span>