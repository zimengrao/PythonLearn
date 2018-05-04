"""
@Name: database
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/4/28
"""

import pymysql
from config import Config
# import time

class DataBase:
    def __init__(self):
        super(DataBase, self).__init__()
        self.config = Config.enum.get('INPUT_DATABASE')

    def testConnect(self, test):
        '''
        测试数据库连接
        :return:
        '''
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='beidi', charset='utf8')      # 打开数据库链接
        cur = conn.cursor()     # 使用cursor() 方法创建一个游标对象cursor
        cur.execute(test)       # 使用execute() 方法执行sql查询
        data = cur.fetchone()   # 使用fetchone() 获取单条数据
        print(data)
        conn.close()

    def selectDate(self, sql):
        """
        查询表数据
        :return:
        """
        # conn = pymysql.connect(INPUT_DATABASE)
        # cur = conn.cursor()
        # data = cur.fetchone(sql)
        pass


    def insertDate(self, field_name, place, sql):

        """

        :param place: 占位符数量
        :param table_name: 别名
        :param sql: 插入sql语句
        :return:
        """

        conn = pymysql.connect(**self.config) # 注意传入的数据为字典类型
        # conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='beidi', charset='utf8')
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()

        for items in data:
            if type(items) == tuple:
                # print(items)
                try:
                    i = 'insert into gt003_user_normal('+field_name+') values('+place+')'
                    cur.execute(i, items)
                    print(items)
                    conn.commit()
                except Exception as err:
                    print(err)
                    conn.rollback()
        conn.close()

    def getItemName(self, sql):

        """
        将传入的sql语句别名，以这种格式tc001_user_id,,tc001_last_ip,tc001_last_time
        :param sql:
        :return: 别名 数组长度
        """

        result = sql.split('FROM')[0].split('SELECT')[1].split(',')  # 取出sql中需要截取的字符串
        print(result)
        field_name = []
        for item in result:
            field_name.append(item.rstrip().split(' ')[-1]) # 将取到的别名，增加到field_name列表中
        length = len(field_name)
        place = ('{}'.format('%s,') * length).rstrip(',')
        # print(length)
        delimiter = ','
        field_name = delimiter.join(field_name)
        return [field_name, place]


# if __name__ == '__main__':
#     getItemName(SQL_AD)
#     insertDate(getItemName(SQL_AD)[0], getItemName(SQL_AD)[1], SQL_AD, **INPUT_DATABASE)


