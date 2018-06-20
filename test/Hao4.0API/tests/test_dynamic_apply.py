"""
@Name: test_dynamic_apply
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/11

"""
import ast
import ddt
import unittest
import json
from lib.client import  HttpHandler
from config.ReadExcel import ExcelData
from lib.business import BusinessApi

data_login = ExcelData('login').readData()
data_giftlist = ExcelData('giftlist').readData()
# data_user = ExcelData().readData('user')

@ddt.ddt
class HqsApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http = HttpHandler()
        cls.lib = BusinessApi()

    @ddt.data(*data_login)
    def test_login_is_ok(self, data_login):
        """登录接口测试"""
        self.data = ast.literal_eval(data_login['body'])
        result = json.loads(self.http.post(self.lib.url, data=self.data))
        print(result)
        self.assertEqual(self.http.get_value(result, 'info'), data_login['info'])
        self.assertEqual(self.http.get_value(result, 'err_msg'), data_login['err_msg'])

    @ddt.data(*data_giftlist)
    def test_giftlist_is_ok(self, data_giftlist):
        """获取礼物列表接口"""
        # self.bus.set_token()
        # self.loginuid = self.bus.set_token()[1]
        # self.token = self.bus.set_token()[0]
        #
        # print(self.loginuid, self.token)
        # data = {
        #     "loginuid": self.loginuid,
        #     "logintoken": self.token,
        #     "params":{
        #         "activity_id": "2f0fc929-58cd-bbc5-403a-0c6d7d18c376"
        #     }
        # }
        #
        # data = json.dumps(data)

        print(data_giftlist['body'])
        result = json.loads(self.http.post(self.lib.url_dev + data_giftlist['api'], data = data_giftlist['body']))
        self.assertEqual(self.http.get_value(result, 'info'), data_giftlist['err_msg'])
        self.assertListEqual(self.http.get_value(result,'gifts'), eval(data_giftlist['gifts']))

