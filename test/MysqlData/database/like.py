"""
@Name: data
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/4/27
"""

"""
@Name: mus
@Version:
@Project: PyCharm
@Author: wangmin
@Data: 2018/4/26
"""

import pymysql
import uuid

# 导入数据库配置

conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='beidi', charset='utf8')
cur = conn.cursor()
# sql = "SELECT *,tou_time from phome_ecms_photo"
cur.execute("SELECT id id,zan zan from phome_ecms_photo where classid in('11','2','3') and truetime>1518537600 and zan!=''")
rs = cur.fetchall()

i = 0
j = 0
for r in rs:
    # print(rs)
    if type(r) == tuple:
        print(r)
        dynamic = r[0]
        print('dynamic={}'.format(dynamic))
        vote = r[1].split('\r\n')
        j += 1
        # print(vote)
        for item in vote[0].split('::::::'):
                if item == '':
                    pass
                else:
                    try:
                        cur.execute("insert into  gt045_advertising(tc045_advert_id,tc045_photo_url,tc045_user_id) values(%s, %s, %s)",('1', '2', '3'))

                        # cur.execute("insert into  gt021_like(tc021_like_id, tc021_mult_id, tc021_user_id) values(%s, %s, %s)",(str(uuid.uuid1()), dynamic, item))
                        conn.commit()
                        i += 1
                    except :
                        conn.rollback()
print('i={}'.format(i))
print('j={}'.format(j))
conn.close()

