"""
@Name: photo
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/5/10
"""

import pymysql
import uuid
import time


# config = {
#     'host': '192.168.1.27',
#     'port': 3306,
#     'user': 'root',
#     'password': '123456',
#     'db': 'beidi',
#     'charset': 'utf8'
# }

# config = {
#     'host': '47.100.60.152',
#     'port': 3306,
#     'user': 'gttest',
#     'password': 'COk+Y5.g8FDxJ5s',
#     'db': 'ceshihao3.6',
#     'charset': 'utf8'
# }
#
config = {
    'host': 'rm-bp11g1br1u79795y5rw.mysql.rds.aliyuncs.com',
    'port': 3306,
    'user': 'zjk',
    'password': 'zjk940915++',
    'db': 'hao',
    'charset': 'utf8'
}

# photo表中的动态图片和报名图片导入到tc019_photo表中
# news_photo 存放了图片动态和图片报名（type=1）
# sql = """
#
#           SELECT id,newstime,new_photo from phome_ecms_photo where new_photo!=''
#
#       """
#
# # 分割用户表中的相册（type=4）
# sql1 = """
#             SELECT userid, '' newstime, photo FROM phome_enewsmemberadd WHERE photo != ''
#        """
#
# #分割点赞表
# sql2 = """
#        SELECT id, zan from phome_ecms_photo where zan!=''
#
#        """
#
# # 粉丝
# sql3 = """
#        SELECT userid, feeduserid from phome_enewsmemberadd where feeduserid!=''
#
#        """



# def photo(sql, tc_type):
#     '''
#     将所有和图片有关的数据全部到导入图片表中
#     :param sql: 查询的sql语句
#     :param tc_type: 相册类型，1：动态图片，2：视频缩略图，3：用户头像 4：用户相册图片
#     :return:
#
#     '''
#     global conn
#     global cur
#     conn = pymysql.connect(**config)
#     cur = conn.cursor()
#     cur.execute(sql)
#     rs = cur.fetchall()
#
#     i = 0
#     j = 0
#
#     for r in rs:
#         # print(rs)
#         if type(r) == tuple:
#             # print(r)
#             dynamic = r[0]
#             time = r[1]
#             vote = r[2].split('\r\n')
#             j += 1
#             vote = vote[0].split('::::::')
#             for item in vote:
#                 if '' in vote:
#                     vote.remove('')
#                 print(vote)
#                 try:
#                     cur = conn.cursor()
#                     cur.execute("insert into  gt019_photo(tc019_photo_id, tc019_mult_id, tc019_time, tc019_url, tc019_type) values(%s, %s, %s, %s, %s)",(str(uuid.uuid1()), dynamic, time, item, tc_type))
#                     conn.commit()
#                     # print(item)
#                     i += 1
#                 except :
#                     conn.rollback()
#                     conn.close()

# def like(sql):
#     '''
#     点赞表
#     :param sql:
#     :return:
#     '''
#
#     conn = pymysql.connect(**config)
#     cur = conn.cursor()
#     cur.execute(sql)
#     rs = cur.fetchall()
#
#     for r in rs:
#         # print(rs)
#         # if type(r) == tuple:
#         dynamic = r[0]
#         vote = r[1].split('::::::')
#         for userid in vote:
#             if '' in vote:
#                 vote.remove('')
#             cur.execute("SELECT username from phome_enewsmember WHERE userid = " + userid)
#             user = cur.fetchall()
#             for username in user:
#                 username = username[0]
#             try:
#                 cur.execute("insert into  gt021_like(tc021_like_id, tc021_mult_id, tc021_user_id, tc021_user_name) values(%s, %s, %s, %s)",(str(uuid.uuid1()), dynamic, userid, username))
#                 conn.commit()
#                 print(dynamic, userid, username)
#             except Exception as err:
#                 print(err)
#                 conn.rollback()
#                 # conn.close()

# def feed(sql):
#     '''
#     将粉丝userid拆分之后，导入4.0数据库中
#     :param sql: 查询3.6数据库用户表，粉丝userid
#     :return:
#     '''
#     conn = pymysql.connect(**config)
#     cur = conn.cursor()
#     cur.execute(sql)
#     rs = cur.fetchall()
#     # print(rs)
#     for r in rs:
#         userid = r[0]
#         feeduserid = r[1].split('::::::')
#         del feeduserid[-1]
#         # print(userid, feeduserid)
#         for feed in feeduserid:
#             print(userid, feed)
#             try:
#                 cur.execute("insert into gt067_fans(tc067_fans_id, tc067_userid_from, tc067_userid_to) values( %s, %s, %s)",(str(uuid.uuid1()), feed, userid))
#                 conn.commit()
#                 # print(userid,feeduserid)
#             except Exception as err:
#                 print(err)
#                 conn.rollback()
#                 conn.close()

# def photo_split():
#     '''
#     将数据库中的图片帖::::::分割改为,分割
#     :return:
#     '''
#     conn = pymysql.connect(**config)
#     cur = conn.cursor()
#     sql = "SELECT tc094_json_photo FROM gt094_dynamic_apply where tc094_json_photo !='';"
#     cur.execute(sql)
#     rs = cur.fetchall()
#
#     for r in rs:
#         r=str(r[0])
#         r_new=r.replace('::::::',',')
#         try:
#             # sql="update gt092_dynamic_short set tc094_json_photo =  where tc094_json_photo =" + r_new,r
#             sql = "update gt094_dynamic_apply set tc094_json_photo= '%s' where tc094_json_photo = '%s'" % (r_new,r)
#             cur.execute(sql)
#             conn.commit()
#             print(r, r_new)
#
#         except Exception as err:
#             print(err)
#             conn.rollback()
#             conn.close()

# def tuijian():
#     '''
#     将旧数据的通过::::::分割的数据存入59表中
#     1、旧数据导入需要保存旧的帖子id
#     :return:
#     '''
#     conn = pymysql.connect(**config)
#     cur = conn.cursor()
#     sql = "SELECT userid, tuijian_shi, lasttime FROM phome_enewsmemberadd where tuijian_shi != '' and newstime>1536120000 and newtime<1536678000;"
#     cur.execute(sql)
#     rs = cur.fetchall()
#
#     for r in rs:
#         userid = r[0]
#         photo_id = r[1].split('::::::')
#         lasttime = r[2]
#         del photo_id[-1]
#         for item in photo_id:
#             # item_time = int(time.time())
#             # print(userid, item, lasttime)
#
#             try:
#                 cur.execute("insert into gt059_recommend_video(tc059_reco_video_id, tc001_user_id, tc091_dyna_rela_id,tc059_time,tc059_reserve1) values( %s, %s, %s, %s, %s)",(str(uuid.uuid1()), userid, item, lasttime,item))
#                 conn.commit()
#
#                 print(userid, item, lasttime)
#             except Exception as err:
#                 print(err)
#                 conn.rollback()
#                 conn.close()
#
# def user_photo():
#     '''
#     琴行和老师用户相册
#     :return:
#     '''
#     conn = pymysql.connect(**config)
#     cur = conn.cursor()
#     sql = "SELECT photo,lasttime,userid FROM phome_enewsmemberadd where photo REGEXP '.png|.jpg|.bmp|.jpeg' and photo != '';"
#     cur.execute(sql)
#     rs = cur.fetchall()
#
#     for r in rs:
#         photo_id = r[0].split('::::::')
#         del photo_id[-1]
#
#         r_time = r[1]
#         userid = r[2]
#         for item in photo_id:
#
#             try:
#                 cur.execute("insert into gt069_user_photo(tc069_user_photo_id, tc001_user_id, tc069_url,tc069_createtime) values( %s, %s, %s, %s)",(str(uuid.uuid1()), userid, item, r_time ))
#                 conn.commit()
#
#                 print(userid, item, r_time)
#             except Exception as err:
#                 print(err)
#                 conn.rollback()
#                 conn.close()
#
# def dynamic_num():
#     '''
#     用户发帖数量
#     :return:
#     '''
#     conn = pymysql.connect(**config)
#     cur = conn.cursor()
#     sql = "SELECT count(*) as num, tc092_user_id FROM gt092_dynamic_short GROUP BY tc092_user_id;"
#     cur.execute(sql)
#     rs = cur.fetchall()
#
#     print(rs)
#     for r in rs:
#         num = r[0]
#         userid = r[1]
#         print(num,userid)
#         try:
#             cur.execute("update gt003_user_normal set tc003_num_dyna = '%s' where  tc001_user_id = '%s'"%(num,userid))
#             conn.commit()
#
#             print(num,userid)
#         except Exception as err:
#             print(err)
#             conn.rollback()
#             conn.close()
#     for r in rs:
#         num = r[0]
#         userid = r[1]
#         print(num,userid)
#         try:
#             cur.execute("update gt004_user_teacher set tc004_num_dyna = '%s' where  tc001_user_id = '%s'"%(num,userid))
#             conn.commit()
#
#             print(num,userid)
#         except Exception as err:
#             print(err)
#             conn.rollback()
#             conn.close()
#     for r in rs:
#         num = r[0]
#         userid = r[1]
#         print(num,userid)
#         try:
#             cur.execute("update gt005_user_store set tc005_num_dyna = '%s' where  tc001_user_id = '%s'"%(num,userid))
#             conn.commit()
#
#             print(num,userid)
#         except Exception as err:
#             print(err)
#             conn.rollback()
#             conn.close()
#     for r in rs:
#         num = r[0]
#         userid = r[1]
#         print(num,userid)
#         try:
#             cur.execute("update gt006_user_brand set tc006_num_dyna = '%s' where  tc001_user_id = '%s'"%(num,userid))
#             conn.commit()
#
#             print(num,userid)
#         except Exception as err:
#             print(err)
#             conn.rollback()
#             conn.close()
#
# def apply_num():
#     '''
#     活动报名数量
#     :return:
#     '''
#     conn = pymysql.connect(**config)
#     cur = conn.cursor()
#     sql = "SELECT count(tc094_id),tc028_act_id FROM gt094_dynamic_apply where tc028_act_id !='' GROUP BY tc028_act_id ;"
#     cur.execute(sql)
#     rs = cur.fetchall()
#
#     print(rs)
#     for r in rs:
#         num = r[0]
#         userid = r[1]
#         print(num,userid)
#         try:
#             cur.execute("update gt028_activity set tc028_apply_num = '%s' where  tc028_act_id = '%s'"%(num,userid))
#             conn.commit()
#
#             print(num,userid)
#         except Exception as err:
#             print(err)
#             conn.rollback()
#             conn.close()
#
#
# def set_username():
#     '''
#     根据userid更新发帖用户名
#     :return:
#     '''
#     conn = pymysql.connect(**config)
#     cur = conn.cursor()
#     sql = "SELECT tc094_id,tc094_user_id FROM gt094_dynamic_apply;"
#     cur.execute(sql)
#     rs = cur.fetchall()
#
#     # print(rs)
#     for r in rs:
#         num = r[0]
#         userid = r[1]
#         # print(num,userid)
#         try:
#             cur.execute("SELECT username FROM phome_enewsmember where userid = '%s';"%userid)
#             rs = cur.fetchone()
#             cur.execute("update gt094_dynamic_apply set tc094_user_name = '%s' where  tc094_id = '%s'"%(rs[0], num))
#             conn.commit()
#
#             print(rs[0], num)
#         except Exception as err:
#             print(err)
#             conn.rollback()
#             # conn.close()

# def like_100():
#     '''
#     更改点赞数据
#     :return:
#     '''
#     conn = pymysql.connect(**config)
#     cur = conn.cursor()
#     sql = "SELECT tc001_user_from,tc100_id FROM `hao`.gt100_message_user where tc100_type=2 and tc100_id>=4172 and tc100_id <=4241;"
#     cur.execute(sql)
#     rs = cur.fetchall()
#
#     # print(rs)
#     for r in rs:
#         user_from = r[0]
#         tc100_id = r[1]
#         # print(user_from)
#         try:
#             cur.execute("SELECT tc002_name FROM `hao`.gt002_user_auth where tc001_user_id='%s' and tc002_login_type='a7d3bbc5-dcb7-53ff-2df1-af203a832b52';"%user_from)
#             # cur.execute(sql)
#             rs = cur.fetchall()
#             print(rs)
#             for r in rs:
#                 cur.execute("update `hao`.gt100_message_user  set tc100_content = concat('%s' , ' 点赞了你的音乐日记') where  tc100_id = '%s'"%((r[0]), tc100_id))
#                 conn.commit()
#                 #
#                 # print(rs[0], num)
#         except Exception as err:
#             print(err)
#             conn.rollback()
            # conn.close()

# def review_100():
#     '''
#     更改点赞数据
#     :return:
#     '''
#     conn = pymysql.connect(**config)
#     cur = conn.cursor()
#     sql = "SELECT tc001_user_from, tc001_user_to, tc100_detail_id,tc100_id,tc100_time FROM `hao`.gt100_message_user where tc100_type=1 and tc100_content like '%评论%' ORDER BY tc100_time DESC;"
#     cur.execute(sql)
#     rs = cur.fetchall()
#
#     # print(rs)
#     for r in rs:
#         tc001_user_from = r[0]
#         tc001_user_to = r[1]
#         tc100_detail_id = r[2]
#         tc100_id = r[3]
#         tc100_time = r[4]
#         # print(user_from)
#         try:
#             cur.execute("SELECT count(*), tc022_content FROM `hao`.gt022_review where tc022_user_id='%s' and tc022_owner_id='%s' and tc022_detail_id='%s' and tc022_time = '%s' order by tc022_time desc;"%(tc001_user_from, tc001_user_to,tc100_detail_id,tc100_time))
#             # cur.execute(sql)
#             qs = cur.fetchall()
#             print(qs)
#             # for q in qs:
#             #     if q[0] == 1:
#             #         print(q[0], q[1])
#             #         cur.execute("update `hao`.gt100_message_user  set tc100_content = '%s' where  tc100_id = '%s'"%(q[1],tc100_id))
#             #         conn.commit()
#                 #
#                 # print(rs[0], num)
#         except Exception as err:
#             print(err)
#             conn.rollback()
#             conn.close()


def activity_28():
    '''
    更改点赞数据
    :return:
    '''
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "SELECT tc001_user_from, tc001_user_to, tc100_detail_id,tc100_id,tc100_time FROM `hao`.gt100_message_user where tc100_type=1 and tc100_content like '%评论%' ORDER BY tc100_time DESC;"
    cur.execute(sql)
    rs = cur.fetchall()

    # print(rs)
    for r in rs:
        tc001_user_from = r[0]
        tc001_user_to = r[1]
        tc100_detail_id = r[2]
        tc100_id = r[3]
        tc100_time = r[4]
        # print(user_from)
        try:
            cur.execute("SELECT count(*), tc022_content FROM `hao`.gt022_review where tc022_user_id='%s' and tc022_owner_id='%s' and tc022_detail_id='%s' and tc022_time = '%s' order by tc022_time desc;"%(tc001_user_from, tc001_user_to,tc100_detail_id,tc100_time))
            # cur.execute(sql)
            qs = cur.fetchall()
            print(qs)
            # for q in qs:
            #     if q[0] == 1:
            #         print(q[0], q[1])
            #         cur.execute("update `hao`.gt100_message_user  set tc100_content = '%s' where  tc100_id = '%s'"%(q[1],tc100_id))
            #         conn.commit()
                #
                # print(rs[0], num)
        except Exception as err:
            print(err)
            conn.rollback()
            conn.close()



if __name__ == '__main__':
    # photo(sql, 1)
    # photo(sql1, 4)
    # like(sql2)
    # feed(sql3)
    # select_openid()
    # select_username_phone()
    # select_phone()
    # photo_split()
    # tuijian()
    # user_photo()
    # dynamic_num()
    # apply_num()
    # set_username()
    # review_100()
