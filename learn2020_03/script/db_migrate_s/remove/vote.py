"""
@Name: mus
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/4/26
"""

import pymysql
import uuid
import  string

# 连接数据库，数据库名为beidi
# conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='beidi', charset='utf8')
conn = pymysql.connect(host='47.100.60.152', port=3306, user='gttest', password='COk+Y5.g8FDxJ5s', db='ceshihao3.6', charset='utf8')

cur = conn.cursor()
# sql = "SELECT *,tou_time from phome_ecms_photo"
cur.execute("SELECT id,tou_time from phome_ecms_photo where tou_time != ''")
rs = cur.fetchall()



# print(rs)
i = 0
for r in rs:
    if type(r) == tuple:
        dynamic = r[0]
        # print('dynamic={}'.format(dynamic))
        vote = r[1].split('\r\n')
        print(dynamic, vote)

        for items in vote:
            if len(items.split('::::::')) == 2:
                userid = items.split('::::::')[0]
                vote_time = items.split('::::::')[1]
                print(userid, vote_time)
                if userid.isdigit():
                    cur.execute("SELECT username from phome_enewsmember WHERE userid = " + userid)
                    username = cur.fetchall()
                    print(username)
                    try:
                        cur.execute(
                            "insert into  gt030_vote(tc030_vote_id, tc091_dyna_id, tc030_user_id, tc030_time, tc030_user_name, tc030_detail_id) values(%s, %s, %s, %s, %s, %s)",
                            (str(uuid.uuid1()), str(uuid.uuid1()), userid, vote_time, username, dynamic))
                        conn.commit()
                        print( userid, vote_time, username, dynamic)
                    except Exception as err:
                        print(err)
                        conn.rollback()

                i += 1

print('i={}'.format(i))
conn.close()
