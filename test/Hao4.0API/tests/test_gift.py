"""
@Name: test_gift
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/22
"""

import unittest
import json
from lib.client import HttpHandler
# from config.ReadExcel import ExcelData
# from lib.business import BusinessApi


class Gift11(unittest.TestCase):

    @classmethod
    def SetUpClass(cls):
        cls.http = HttpHandler()
        # cls.lib = BusinessApi()

    def test_gift_is_ok(self):
        data = {
            "loginuid": "48623",
            "logintoken": "NyXcmv4gK3RDSThw5LNZ",
            "params":{
                "gift_id": "dd39368f-c3ef-e692-3d2d-c78f6a167d02",
                "num": "1",
                "accept_id": "48844",
                "detail_id": "18897"
            }
        }

        data = json.dumps(data)
        print(data)
        # self.http.post('1', data = data)
        resp = json.loads(self.http.post('http://dev4.0.greattone.com/index.php?r=record-gift/create', data = data))
        print(resp)