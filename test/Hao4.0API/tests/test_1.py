"""
@Name: test_1
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/28
"""

import unittest
import json
from lib.client import HttpHandler
# from lib.business import BusinessApi

# data_login = ExcelData('login').readData()
# data_giftlist = ExcelData('giftlist').readData()
# # data_user = ExcelData().readData('user')

class HqsApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http = HttpHandler()
        # cls.lib = BusinessApi()

    def test_login_is_ok(self):
        self.data = {
            "loginuid": "48623",
            "logintoken": "NyXcmv4gK3RDSThw5LNZ",
            "params":{
                "gift_id": "dd39368f-c3ef-e692-3d2d-c78f6a167d02",
                "num": "1",
                "accept_id": "48844",
                "detail_id": "18897"
            }
        }

        self.data = json.dumps(self.data)
        print(self.data)
        # self.http.post('1', data = data)
        resp = json.loads(self.http.post('http://dev4.0.greattone.com/index.php?r=record-gift/create', data = self.data))
        print(resp)



