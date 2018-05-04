"""
@Name: user
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/4/28
"""

import pymysql
import uuid
import time
import sys
import io
import urllib.request
import hashlib

conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='beidi', charset='utf8')
cur = conn.cursor()
cur.execute("SELECT phome_enewsmember.userid,openid,username,registertime,laiyuan from phome_enewsmember,phome_enewsmemberadd where phome_enewsmember.userid = phome_enewsmemberadd.userid and phome_enewsmember.openid != '' AND phome_enewsmemberadd.laiyuan='wx' ")
SQL_AD = "SELECT adid tc045_advert_id, picurl tc045_photo_url, url tc045_url, pic_width tc045_width, pic_height tc045_height, onclick tc045_click, title tc045_name, CONCAT(starttime) tc045_time_start, CONCAT(endtime) tc045_time_end, adsay tc045_describe FROM phome_enewsad where picurl !='' or url !=''"

# cur.execute("SELECT phome_enewsmember.userid,registertime,regip,lastip,lasttime,laiyuan FROM phome_enewsmember LEFT JOIN phome_enewsmemberadd on phome_enewsmember.userid = phome_enewsmemberadd.userid where phome_enewsmember.userid>85368")
rs = cur.fetchall()
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


i = 0
for r in rs:
    if type(r) == tuple:
        # print(r)
        # tc001_user_id = r[0]
        # tc001_regtime = r[1]
        # tc001_register_ip = r[2]
        # tc001_last_ip = r[3]
        # tc001_last_time = r[4]
        # tc001_source = r[5]
        # print(userid, regtime, regip, lastip, lasttime, laiyuan)
        user_id = r[0]
        username = r[2]
        openid = r[1]
        createtime = r[3]
        laiyuan = r[4]
        # openid = hashlib.md5(login_name.encode(encoding='utf-8')).hexdigest()
        try:
            cur.execute("insert into  gt002_user_auth1(tc002_user_auth_id, tc001_user_id, tc002_login_type, tc002_user_name,tc002_openid,tc002_createtime) values(%s, %s, %s, %s, %s, %s)",(str(uuid.uuid1()), user_id, laiyuan, username, openid, createtime))
            # cur.execute("insert into  gt001_user(tc001_user_id, tc001_regtime, tc001_register_ip, tc001_last_ip, tc001_last_time, tc001_source) values(%s, %s, %s, %s, %s, %s)",(tc001_user_id, tc001_regtime, tc001_register_ip, tc001_last_ip, tc001_last_time, tc001_source))
            conn.commit()
        except :
            conn.rollback()
        i += 1
        print('i={}'.format(i))

print('i={}'.format(i))
conn.close()
