"""
@Name: delete_repeat_user
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/9/2
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
#
config = {
    'host': '47.100.60.152',
    'port': 3306,
    'user': 'gttest',
    'password': 'COk+Y5.g8FDxJ5s',
    'db': 'ceshihao3.6',
    'charset': 'utf8'
}

# config = {
#     'host': 'rm-bp11g1br1u79795y5.mysql.rds.aliyuncs.com',
#     'port': 3306,
#     'user': 'zjk',
#     'password': 'zjk940915++',
#     'db': 'hao',
#     'charset': 'utf8'
# }

def select_phone():
    '''
    1、查询memberadd表中，phone字段重复的数据
    2、查询此用户有没有在photo表中有没有数据
    3、将未发帖的用户，筛选出来
    4、手机号重复数据是以所有用户未筛选条件
    5、有发帖的用户，将手机号全部置为空
    update phome_enewsmember set username = '' where userid in ('14554')
    6、将未发帖手机号码重复的用户删除，将有发帖，手机号码置为空
    7、select_openid和select_username_phone这两个方法
    ！！！6、注意删除的时候，一定要以时间排序查看是否可删除
    :return:
    '''
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql="select userid from phome_enewsmemberadd where phone in (select phone from phome_enewsmemberadd group by phone having count(1) > 1) and phone!='';"
    cur.execute(sql)
    rs = cur.fetchall()
    i = 0
    j = 0
    list_userid = []
    userid = []
    for r in rs:

        # print(r[0])
        sql="SELECT * from phome_ecms_photo where userid = " + str(r[0])
        cur.execute(sql)
        rs = cur.fetchall()
        if rs:
            userid.append(str(r[0]))
            j += 1
        else:
            list_userid.append(str(r[0]))
            i += 1
    print('重复手机号码,未发帖用户: 一共{}个用户; 用户id：{}'.format(i, list_userid))
    print('重复手机号码,有发帖用户: 一共{}个用户, 用户id：{}'.format(j, userid))

def select_openid():
    '''
    1、查询member表中，openid字段重复的数据
    2、查询此用户有没有在photo表中有没有数据
    3、将未发帖的用户，筛选出来
    :return:
    '''
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql="select userid from phome_enewsmember where openid in (select openid from phome_enewsmember group by openid having count(1) > 1) and openid!=''"
    cur.execute(sql)
    rs = cur.fetchall()
    i=0
    j=0
    list_userid = []
    userid = []
    for r in rs:

        # print(r[0])
        sql="SELECT * from phome_ecms_photo where userid = " + str(r[0])
        cur.execute(sql)
        rs = cur.fetchall()
        if rs:
            userid.append(str(r[0]))
            j += 1
        else:
            list_userid.append(str(r[0]))
            i += 1
    print('重复openid,未发帖用户: 一共{}个用户, 用户id：{}'.format(i, list_userid))
    print('重复openid,有发帖用户: 一共{}个用户, 用户id：{}'.format(j, userid))


def select_username_phone():
    '''
    1、查询member表和memberadd表中的，username与phone字段相同的所有数据
    2、查询此用户有没有在photo表中有没有数据
    3、将未发帖的用户，筛选出来
    4、无用户条件筛选
    5、/* 重复数据，给member表中username拼接赋值 */
       update phome_enewsmember set username = concat('hqs_', username) where userid in ('14554')
    :return:
    '''
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql="select a.userid,a.username,b.userid,b.phone from phome_enewsmember a,phome_enewsmemberadd  b where a.username =b.phone group by a.userid desc"
    cur.execute(sql)
    rs = cur.fetchall()
    i=0
    list_userid = []
    userid1 = []
    j=0
    for r in rs:

        # print(r[0])
        sql="SELECT * from phome_ecms_photo where userid = " + str(r[0])
        cur.execute(sql)
        rs = cur.fetchall()
        # print(rs)
        if rs:
            userid1.append(str(r[0]))
            j += 1
        else:
            list_userid.append(str(r[0]))
            i += 1
    print('重复username和phone,有发帖用户: 一共{}个用户, 用户id：{}'.format(i, userid1))
    print('重复username和phone,没有发帖用户: 一共{}个用户, 用户id：{}'.format(j, list_userid))

def userid():
    '''
    :return:
    '''
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql="select b.id from (select a.id from (select MAX(tc092_id) as id from gt092_dynamic_short GROUP BY tc092_reserve3) a) b"
    cur.execute(sql)
    rs = cur.fetchall()
    # print(rs)
    userid = []
    # print(list_userid)
    for r in rs:
        print(r[0])
        cur.execute("delete from gt092_dynamic_short where tc092_id = '%s'",r[0])
        # userid.append(r[0])
    # print(userid)


# select_phone()
# select_openid()
# select_username_phone()
userid()