"""
@Name: test_dynamic_apply
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/11

"""

import ddt
import unittest
import json
from lib.client import  HttpHandler
from config.data import ExcelData
from lib.business import BusinessApi
from config.cnf import Config

data_login = ExcelData().readData('login')
data_giftlist = ExcelData().readData('giftlist')
# data_user = ExcelData().readData('user')

@ddt.ddt
class DynamicApply(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http = HttpHandler()
        cls.bus = BusinessApi()
        cls.config = Config()
        cls.loginuid = cls.config.get_config('DATABASE', 'loginuid')
        cls.token = cls.config.get_config('DATABASE', 'token')

    @ddt.data(*data_login)
    def test_login_is_ok(self, data_login):
        """登录接口测试"""
        self.data = json.loads(data_login['body'])
        result = json.loads(self.http.post(self.bus.url, data=self.data))
        print(result)
        self.assertEqual(self.http.get_value(result, 'info'), data_login['info'])
        self.assertEqual(self.http.get_value(result, 'err_msg'), data_login['err_msg'])

    @ddt.data(*data_giftlist)
    def test_giftlist_is_ok(self, data_giftlist):
        """获取礼物列表接口"""
        self.bus.set_token()
        self.loginuid = self.bus.set_token()[1]
        self.token = self.bus.set_token()[0]

        print(self.loginuid, self.token)
        data = {
            "loginuid": self.loginuid,
            "logintoken": self.token,
            "params":{
                "activity_id": "2f0fc929-58cd-bbc5-403a-0c6d7d18c376"
            }
        }

        data = json.dumps(data)

        result = json.loads(self.http.post(self.bus.url_dev + data_giftlist['api'], data = data))
        self.assertEqual(self.http.get_value(result, 'info'), data_giftlist['err_msg'])
        self.assertListEqual(self.http.get_value(result,'gifts'), eval(data_giftlist['gifts']))

