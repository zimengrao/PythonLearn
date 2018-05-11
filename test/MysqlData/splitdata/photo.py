"""
@Name: photo
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/5/10
"""

import pymysql
import uuid


config = {
    'host': '192.168.1.27',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'beidi',
    'charset': 'utf8'
}

# photo表中的动态图片和报名图片导入到tc019_photo表中
# news_photo 存放了图片动态和图片报名
sql = """

          SELECT id,newstime,new_photo from phome_ecms_photo where new_photo!=''

      """

# 分割用户表中的相册
sql1 = """
            SELECT userid, '' newstime, photo FROM phome_enewsmemberadd WHERE photo != ''
       """

#分割点赞表
sqln = """
       SELECT id, zan from phome_ecms_photo where zan!=''

       """


def photo(sql, tc_type):
    '''

    :param sql: 查询的sql语句
    :param tc_type: 相册类型，1：动态图片，2：视频缩略图，3：用户头像 4：用户相册图片
    :return:

    '''
    global conn
    global cur
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    cur.execute(sql)
    rs = cur.fetchall()

    i = 0
    j = 0

    for r in rs:
        # print(rs)
        if type(r) == tuple:
            # print(r)
            dynamic = r[0]
            time = r[1]
            vote = r[2].split('\r\n')
            j += 1
            vote = vote[0].split('::::::')
            for item in vote:
                if '' in vote:
                    vote.remove('')
                print(vote)
                try:
                    cur = conn.cursor()
                    cur.execute("insert into  gt019_photo(tc019_photo_id, tc019_mult_id, tc019_time, tc019_url, tc019_type) values(%s, %s, %s, %s, %s)",(str(uuid.uuid1()), dynamic, time, item, tc_type))
                    conn.commit()
                    # print(item)
                    i += 1
                except :
                    conn.rollback()
                    conn.close()

def like(sql):

    conn = pymysql.connect(**config)
    cur = conn.cursor()
    cur.execute(sql)
    rs = cur.fetchall()

    for r in rs:
        # print(rs)
        # if type(r) == tuple:
        dynamic = r[0]
        vote = r[1].split('::::::')
        for userid in vote:
            if '' in vote:
                vote.remove('')
            cur.execute("SELECT username from phome_enewsmember WHERE userid = " + userid)
            user = cur.fetchall()
            for username in user:
                username = username[0]
            try:
                cur.execute("insert into  gt021_like(tc021_like_id, tc021_mult_id, tc021_user_id, tc021_user_name) values(%s, %s, %s, %s)",(str(uuid.uuid1()), dynamic, userid, username))
                conn.commit()
                print(dynamic, userid, username)
            except:
                conn.rollback()
                conn.close()

if __name__ == '__main__':
    # photo(sql, 1)
    # photo(sql1, 4)
    like(sqln)
