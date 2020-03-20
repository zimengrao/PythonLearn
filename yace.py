"""
@Name: yace.py
@Version: 
@Project: PyCharm
@Author: DN-SH-148
@Data: 2019/12/2
"""

import requests
import json
import logging
import threading

import os
import shutil
import pymysql
import urllib
import re
import string


requrl = 'https://ash.52iuh.com/ash-app/preferential/merchant/index'



logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

restime = []
ok = []


config = {
    'host': '192.168.31.208',
    'port': 3306,
    'user': 'test',
    'password': 'Test#2019',
    'db': 'ash',
    'charset': 'utf8'
}

conn = pymysql.connect(**config)
cur = conn.cursor()

class Restime():

    def run(self, URL, data, headers):
        self.API(URL, data, headers)


    def API(self, URL2, data, headers):
        try:
            r = requests.post(URL2, data=json.dumps(data), headers=headers, verify=False)
            r.raise_for_status()
            # print(r.raise_for_status())
        except requests.RequestException as e:
            print(e)
        else:
            js = json.dumps(r.json())
            return [r.json(), r.elapsed.total_seconds(), js]

    def circulation(self, num, URL2, data, headers):
        for i in range(num):
            restime.append(Restime.API(URL2, data, headers)[1])
            if json.loads(Restime.API(URL2, data, headers)[2])["msg"] == 'ok':
                ok.append(json.loads(Restime.API(URL2, data, headers)[2])["msg"])
                logger.info('请求第' + str(i + 1) + '次，请求' + json.loads(Restime.API(URL2, data, headers)[2])["msg"] + ',状态码：' +
                            json.loads(Restime.API(URL2, data, headers)[2])["code"])
            else:
                logger.info('请求第' + str(i + 1) + '次，请求' + json.loads(Restime.API(URL2, data, headers)[2])["msg"] + ',状态码：' +
                            json.loads(Restime.API(URL2, data, headers)[2])["code"])

        print('测试次数：', num)
        print('响应次数：', len(restime))
        print('正常响应次数：', len(ok))
        print('总响应最大时长(s)：', max(restime))
        print('总响应最小时长(s)：', min(restime))
        print('总响应时长(s)：', sum(restime))
        print('平均响应时长(s)：', sum(restime) / len(restime))

    def he_merchant_coupon(self, URL, data, headers):

        cur.execute("SELECT user_id FROM ash.yyh_merchant_coupon_receive_info where status=1 and"
                    " end_use_time>now() and start_use_time < now();")

        user_id = cur.fetchall()
        # list_recievt= []
        for i in user_id:
            cur.execute("SELECT barcode, template_id FROM ash.yyh_merchant_coupon_receive_info where status=1 and"
                        " end_use_time>now() and start_use_time < now() and user_id=%s limit 6;"%(i))
            recieve=cur.fetchall()
            for item in recieve:
                data['barcode'] = item[0]
                template_id = item[1]
                cur.execute("SELECT merchant_id FROM ash.yyh_merchant_coupon_relation where template_id = '%s' limit 1;"%(template_id))
                merchant_id = cur.fetchall()
                data['merchantId'] = merchant_id[0][0]

                print(data)
                # re = self.API(URL, data, headers=headers)

                t1 = threading.Thread(target=self.run(URL, data, headers))
                t1.start()

    def he_supermarket_coupon(self, URL, data, headers):

        cur.execute("SELECT user_id FROM  `ash`.`yyh_coupon_receive_info` WHERE status=1 and"
                    " endUseTime>now() and startUseTime < now() limit 1;")

        user_id = cur.fetchall()
        # print(user_id)
        # list_recievt= []
        for i in user_id:
            # cur.execute("SELECT merchant_id,barcode FROM ash.yyh_merchant_coupon_receive_info where status=1 and"
            #             " end_use_time>now() and start_use_time < now() and user_id='%s' limit 6;"%(i))

            # cur.execute("SELECT ticketTemplateId, barcode, shopId  FROM  `ash`.`yyh_coupon_receive_info` WHERE status=1 and"
            #             " endUseTime>now() and startUseTime < now() and user_id='%s' limit 6;"%(i))

            cur.execute(
                "SELECT ticketTemplateId, barcode, shopId  FROM  `ash`.`yyh_coupon_receive_info` WHERE status=1 and"
                " endUseTime>now() and startUseTime < now() order by id desc limit 1;")

            recieve=cur.fetchall()

            # print(recieve)

            for item in recieve:
                template_list = []
                barcode_list = []
                template_list.append(str(item[0]))
                barcode_list.append(item[1])
                # user_list.append(item[2])
                data['batchTicketTemplateId'] = template_list
                data['batchBarcode'] = barcode_list
                data['shopId'] = str(item[2])
                data['openid'] = str(i[0])

                print(item[2], type(str(item[2])))
                print(data)
                # print(type(list(str(item[0]))))
                re = self.API(URL, data, headers=headers)
                t1 = threading.Thread(target=self.run(URL, data, headers))
                t1.start()



    # def heXiao(self, URL, data, headers):
    #
    #     for item in self.readDB():
    #         print(item)
    #         # self.API(URL, data, headers=headers)
    #         data['barcode'] = item[1]
    #         data['merchantId'] = item[0]
    #         print(data)
    #         # re = self.API(URL, data, headers=headers)
    #
    #         t1 = threading.Thread(target=self.run(URL, data, headers))
    #         t1.start()
    #
    #         # print(re)
    #         # if json.dumps(re).code == 200:
    #         #     print(data.barcode)

    def hexiao_supermarket(self, userid, couponid):
        # cur.execute("select * from ash.yyh_coupon_receive_info where user_id=%s and campId=%s order by id desc limit 1;")
        cur.execute("select * from ash.yyh_coupon_receive_info where user_id=101012 and campId=%s order by id desc limit 1;")



if __name__ == '__main__':
    Restime = Restime()
    headers = {
        'Content-Type': 'application/json;charset=utf-8',

        'jwtToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcGVuaWQiOiJvVlREVTVOanlOX1Fsc0NJR3BRcjRZc0g2Y1BFIiwic2Vzc2lvbklkIjoib1ZURFU1Tmp5Tl9RbHNDSUdwUXI0WXNINmNQRSIsImV4cCI6MTU4NDAwNjEyOH0.WHvAf4cfWTNdgsZAksE3mCLBl7mEDf_XGl1d8mDhVHQ'
    }
    num = 500
    # URL2 = 'https://ash.52iuh.com/ash-app/preferential/merchant/index'
    URL3 = 'https://asht.52ash.cn/ash-app/merchant/coupon/use'
    URL4 = 'https://asht.52ash.cn/ash-app/mq/useMessage/add'
    dataparams = {
        "latitude": 31.209665298461914,
        "longitude": 121.4708023071289,
        "cityCode": "杭州市",
        "timestamp": 1575221855671,
        "version": "1.5.4"
        }

    dataparams1 = {"barcode": "8500000000731", "merchantId": "20191112367771", "timestamp": 1575343268061, "version": "1.5.4"}
    # Restime.he_merchant_coupon(URL3, dataparams1, headers)

    dataparams2 = {
        "batchTicketTemplateId": ["200003171"],
        "openid": "66361",
        "batchBarcode": ["725037600006203531"],
        "changeMoney": 5,
        "shopId": "1232",
        "posNo": "100001",
        "listNo": "100002",
        "changeTime": "2019-12-30 10:55:00",
        "verifyTime": "2019-12-30 10:55:01"
    }

    Restime.he_supermarket_coupon(URL4, dataparams2, headers)