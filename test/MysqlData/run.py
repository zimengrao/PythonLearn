"""
@Name: jk
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/5/3
"""

# <span style="font-size:24px;"> #简单的图形界面GUI（Graphical User Interface）
from tkinter import *
from lib.database import DataBase
import tkinter.messagebox as messagebox
from tkinter.filedialog import askopenfilename
import os
import io

class Application(Frame):   #从Frame派生出Application类，它是所有widget的父容器
    def __init__(self,master = None):#master即是窗口管理器，用于管理窗口部件，如按钮标签等，顶级窗口master是None，即自己管理自己
        Frame.__init__(self,master)
        self.quitButton = Button(self,text = 'quit',command = self.quit)#创建一个Quit按钮，实现点击即退出窗口
        self.nameButton = Button(self,text = 'hello',command = self.run)#创建一个hello按钮，点击调用hello方法，实现输出
        # self.pathButton = Button(self,text = 'open file',command = self.selectPath)#创建一个hello按钮，点击调用hello方法，实现输出
        self.pack()#将widget加入到父容器中并实现布局
        self.createWidgets()
        self.database = DataBase()

    def createWidgets(self):
        self.helloLabel = Label(self,text = 'hi')#创建一个标签显示内容到窗口
        self.helloLabel.pack()
        # self.pathButton = Button(self, text='open file', command=self.selectPath)
        # self.pathButton.pack()
        self.input = Entry(self)#创建一个输入框，以输入内容
        self.input.pack()
        self.input_table = Entry(self)  # 创建一个输入框，以输入内容
        self.input.pack()
        self.nameButton = Button(self, text='run', command=self.run)
        self.nameButton.pack()
        self.quitButton.pack()

    # def selectPath(self):
    #     path = askopenfilename()
    #     return path

    # def sqlData(self):
        # path = self.selectPath()
        # f = open(self.sql, 'w+', encoding='utf8')
        # content = f.readlines
        # content = f.read()
        # print(content)
        # for i in f.read():
        #     print(i)

    def run(self):
        sql = self.input.get()#获取输入的内容
        value = self.database.getItemName(sql)
        self.database.insertDate(value[0], value[1], sql)
        messagebox.showinfo('Message','hello,%s' %sql)#显示输出


if __name__ == '__main__':

    app = Application()
    app.master.title("mysql")#窗口标题
    app.mainloop()#主消息循环</span>