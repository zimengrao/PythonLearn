"""
@Name: Locust
@Version: 
@Project: PyCharm
@Author: DN-SH-148
@Data: 2019/12/2
"""

import redis
import pymysql
import random

# 测试环境数据库
database = {
    'host': '192.168.31.208',
    'port': 3306,
    'user': 'test',
    'password': 'Test#2019',
    'db': 'ash',
    'charset': 'utf8'
}

conn = pymysql.connect(**database)
cur = conn.cursor()

# 测试环境redis
pool = redis.ConnectionPool(host='192.168.31.208', port=6379, password='yyh-test#2018', decode_responses=True)
r = redis.Redis(connection_pool=pool)



key_list = []
def delete_user_redis(token):
    userid = r.get('token:userId:' + token)
    # print(userid, type(userid))
    key_list.append('token:userId:' + token)
    key_list.append('new:user:device:account:info:' + userid)
    key_list.append('new:user:userId:basic:info:' + userid)
    openid = (r.get('new:user:device:account:info:' + userid)).split('"')[19]
    key_list.append('jwt_token_' + openid)
    key_list.append('new:user:openId:basic:info:' + openid)
    key_list.append('new:wx:user:login:' + openid)

    for i in key_list:

        if r.get(i) != None:
            r.delete(i)
            print(r.get(i))



def phoneNORandomGenerator():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
               "155", "156", "157", "158", "159", "186", "187", "188", "189", "190"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


def delete_userdata(token):
    userid = r.get('token:userId:' + token)
    i = 0
    while i == false:
        phone = phoneNORandomGenerator()
        if cur.execute("SELECT count(*) FROM ash.mini_user_info where phoneNumber='%s';" %(phone)) == 1:
            i = 0
        else:
            cur.execute("update mini_user_info set unionid='' and phoneNumber='%s' where id = '%s';" % (phone, userid))
            cur.execute("delete from `ash`.`yyh_user_device_account` where user_id = '%s';" % userid)
            i = 1





if __name__ == '__main__':
    # delete_userdata('d2ff7dfd3de44042af6a7470711430d5')
    delete_user_redis('ce20e9f5eded47c48ae11e48b1573cc3')