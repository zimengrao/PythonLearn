"""
@Name: token
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/11
"""

import json

#
# from config.cnf import Config
from lib.client import HttpHandler
# from lib.business import BusinessApi
from config.data import ExcelData
import ddt
import unittest


# data_login = ExcelData('login').next()
data_giftlist = ExcelData('giftlist').next()
# token = None
# loginuid = None
# print(self.loginuid, self.token)
# @ddt.ddt
# class DynamicApply(unittest.TestCase):
#     def __init__(self):
#         pass

# @ddt.data(*data_giftlist)
def yy():
    http = HttpHandler()
    data = {
        "loginuid": 647550,
        "logintoken": 'VfghYy92wZEqHbYKxGCk',
        "params": {
            "activity_id": "2f0fc929-58cd-bbc5-403a-0c6d7d18c376"
        }
    }

    data = json.dumps(data)

    result = json.loads(http.post('http://dev4.0.greattone.net/index.php?r=activity-gift/index', data=data))
    # print(result)
    # pp = data_giftlist['gifts']
    # print(pp)
    # print(type(data_giftlist['gifts']))

    # self.assertEqual(self.http.get_value(result, 'info'), data_giftlist['err_msg'])
    print(http.get_value(result, 'gifts'))
    print(type(http.get_value(result, 'gifts')))


    # gifts_data = json.loads(http.get_value(result, 'gifts'))

if __name__ == '__main__':
    yy()
