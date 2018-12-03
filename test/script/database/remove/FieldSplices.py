"""
@Name: ceshi
@Version:
@Project: PyCharm
@Author: wangmin
@Data: 2018/5/4
"""

import pymysql

config = {
    'host': '47.100.60.152',
    'port': 3306,
    'user': 'gttest',
    'password': 'COk+Y5.g8FDxJ5s',
    'db': 'ceshihao3.6',
    'charset': 'utf8'
}

# config = {
#     'host': '192.168.1.27',
#     'port': 3306,
#     'user': 'root',
#     'password': '123456',
#     'db': 'beidi',
#     'charset': 'utf8'
# }

# 全站类型表，tc090_tag 字段拼接，父类：父类名称 子类：子类名称+父类名称

conn = pymysql.connect(**config)
cur = conn.cursor()
# sql = "SELECT *,tou_time from phome_ecms_photo"
cur.execute(
    "SELECT tc090_name, tc090_parent_id, tc090_global_type_id  from gt090_global_type")
rs = cur.fetchall()

global name

for r in rs:
    print(r)
    tc090_name = r[0]
    tc090_parent_id = r[1]
    tc090_global_type_id = r[2]
    # print(tc090_parent_id)
    if tc090_parent_id.strip() == '':
        try:
            sql = "update gt090_global_type SET tc090_tag = '%s' WHERE tc090_global_type_id = '%s'" %(tc090_name,tc090_global_type_id)
            cur.execute(sql)
            print(sql)
            conn.commit()
        except:
            conn.rollback()
    else:
        cur.execute("SELECT tc090_name  from gt090_global_type WHERE tc090_global_type_id = '%s'" % (tc090_parent_id))
        r2 = cur.fetchall()
        for r3 in r2:
            # global name
            # print(r3[0])
            name = r3[0] + '_' + r[0]
            # print(name)
            try:
                cur.execute(
                    "update gt090_global_type SET tc090_tag = '%s' WHERE tc090_parent_id != '' and tc090_global_type_id = '%s'" % (
                    name, tc090_global_type_id))
                conn.commit()
            except:
                conn.rollback()
                conn.close()

