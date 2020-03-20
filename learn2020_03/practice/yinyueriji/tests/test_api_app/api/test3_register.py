"""
@Name: test_homepage
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/12/18
"""

"""
@Name: test2_login_check
@Version:
@Project: PyCharm
@Author: wangmin
@Data: 2019/1/7
"""

import json
import unittest
import ddt

from lib.web.business import BusinessApi
from lib.web.client import HttpHandler
from config.ReadExcel import ExcelData
from config.cnf import Config
from config.mysql import MysqlData

data= ExcelData('appapi').readData()

@ddt.ddt
class HqsApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http = HttpHandler()
        cls.lib = BusinessApi()
        cls.mysql = MysqlData()
        cls.config = Config()

    @ddt.data(*data[30:35])
    def test5_check_login_is_ok(self, data):
        ''' 登录失败验证 '''
        post_data = data['Request_Data']
        post_data = post_data.encode('utf-8')
        result = json.loads(self.http.post(self.lib.appapi_url + data['Request_URL'], data=post_data))
        self.case_name = data['API_Purpose']
        self.assertEqual(data['Check_Point'], self.http.get_value(result, 'info'))
        print(result)


    @ddt.data(*data[35:37])
    def test5_check_login_is_ok(self, data):
        ''' 登录成功验证 '''
        post_data = data['Request_Data']
        post_data = post_data.encode('utf-8')
        result = json.loads(self.http.post(self.lib.appapi_url + data['Request_URL'], data=post_data))
        self.case_name = data['API_Purpose']
        self.assertEqual(data['Check_Point'], self.http.get_value(result, 'info'))
        print(result)
