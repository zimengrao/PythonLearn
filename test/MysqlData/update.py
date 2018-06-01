"""
@Name: run1
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/5/4
"""

# <span style="font-size:24px;"> #简单的图形界面GUI（Graphical User Interface）
from tkinter import *
import pymysql

config = {
    'host': 'rm-bp11g1br1u79795y5.mysql.rds.aliyuncs.com',
    'port': 3306,
    'user': 'zjk',
    'password': 'zjk940915++',
    'db': 'hao',
    'charset': 'utf8',
}

# config = {
#     'host': '47.100.60.152',
#     'port': 3306,
#     'user': 'gttest',
#     'password': 'COk+Y5.g8FDxJ5s',
#     'db': 'ceshihao3.6',
#     'charset': 'utf8',
# }


root = Tk()
root.title("hello world")                #是x 不是*


id_before = Label(root, text="before_change_shop_id:").grid(row = 0, column = 0)
before_data = StringVar()
id_before_data = Entry(root, textvariable = before_data).grid(row = 0, column = 1)
before_data.set(" ")

id_behind = Label(root, text='behind_change_shop_id:').grid(row = 1, column = 0)
behind_data = StringVar()
id_behind_data = Entry(root, textvariable = behind_data).grid(row = 1, column = 1)
behind_data.set(" ")

def setDate(id_behind, id_before):
    """

    :param place: 占位符数量
    :param table_name: 别名
    :param sql: 插入sql语句
    :return:
    """

    conn = pymysql.connect(**config)  # 注意传入的数据为字典类型
    # conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='beidi', charset='utf8')
    cur = conn.cursor()
    sql1 = 'UPDATE phome_ecms_photo SET hai_id = '+id_behind+',hai_division = (SELECT title from phome_ecms_shop where id ='+id_behind+')WHERE hai_id = '+id_before+';'
    sql2 = 'UPDATE phome_enewsshopdd SET titid = '+id_behind+' WHERE titid = '+id_before+';'

    # print(sql1)
    try:
        cur.execute(sql1)
        conn.commit()
        cur.execute(sql2)
        conn.commit()
        print(id_before)
    except Exception as err:
        print(err)
        conn.rollback()
    conn.close()
def click():
    id_before = before_data.get()
    id_behind = behind_data.get()

    setDate(id_behind, id_before)

    # string = str("xls名：%s " % x)
    # print(id_before, id_behind)

Button(root, text="press", command=click).grid(row =2 , column = 0)

root.mainloop()