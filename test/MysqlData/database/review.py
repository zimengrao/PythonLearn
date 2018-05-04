"""
@Name: mus
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/4/26
"""

import pymysql
import uuid
import time

# 连接数据库，数据库名为beidi
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='beidi', charset='utf8')
cur = conn.cursor()
# sql = "SELECT *,tou_time from phome_ecms_photo"
cur.execute("SELECT id,tou_time from phome_ecms_photo where classid='73' and truetime>1518537600")
rs = cur.fetchall()
# uuid = str(uuid.uuid1())
# for r in rs:
#     print(r)

# rs = (18452, '48844::::::2018-04-17 10:46:02\r\n8530::::::2018-04-16 17:45:08\r\n')


# print(rs)
i = 0
j = 0
for r in rs:
    if type(r) == tuple:
        dynamic = r[0]
        print('dynamic={}'.format(dynamic))
        vote = r[1].split('\r\n')
        j += 1
        print('j={}'.format(j))
        for items in vote:
            if len(items.split('::::::')) == 2:
                userid = items.split('::::::')[0]
                vote_time = items.split('::::::')[1]
                try:
                    cur.execute("insert into  gt030_vote(tc030_vote_id, tc091_dyna_rela_id, tc030_user_id, tc030_time) values(%s, %s, %s, %s)",(str(uuid.uuid1()), dynamic, userid, vote_time))
                    conn.commit()
                except :
                    conn.rollback()

print('i={}'.format(i))
print('j={}'.format(j))
conn.close()
