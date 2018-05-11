"""
@Name: ceshi
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/5/4
"""

"""
@Name: photo
@Version:
@Project: PyCharm
@Author: wangmin
@Data: 2018/5/10
"""

import pymysql
import uuid
from config import Config
# 导入数据库配置

class IsPhoto():

    def __init__(self):
        self.config = Config.enum
    def selcetDate(self, sql):
        conn = pymysql.connect(**self.config)
        cur = conn.cursor()
        cur.execute(sql)
        rs = cur.fetchall()
        return rs

    def insert_Date(self):
        i = 0
        j = 0
        sql = """

                      SELECT id,newstime,new_photo from phome_ecms_photo where new_photo!=''

                  """
        for r in self.selcetDate(sql):
            # print(rs)
            if type(r) == tuple:
                # print(r)
                dynamic = r[0]
                time = r[1]
                vote = r[2].split('\r\n')
                j += 1
                # print(vote)
                # print(type(vote))
                for item in vote[0].split('::::::'):
                    try:
                        conn = pymysql.connect(**self.config)
                        cur = conn.cursor()
                        cur.execute("insert into  gt019_photo(tc019_photo_id, tc019_mult_id, tc019_time, tc019_url) values(%s, %s, %s, %s)",(str(uuid.uuid1()), dynamic, time, item))
                        conn.commit()
                        print(item)
                        i += 1
                    except :
                        conn.rollback()
                        conn.close()


