
"""
@Name: test_status
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/9/21
"""
import ddt
import unittest
import json
from lib.client import HttpHandler
from config.ReadExcel import ExcelData
from lib.business import BusinessApi
from config.mysql import MysqlData
from config.cnf import Config

data= ExcelData('webapi').readData()

@ddt.ddt
class HqsApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http = HttpHandler()
        cls.lib = BusinessApi()
        cls.mysql = MysqlData()
        cls.config = Config()

    @ddt.data(*data[116:117])
    def test1_home_is_ok(self, data):
        """ 首页 """
        resp = self.http.post_code(self.lib.api + data['Request_URL'], data=data['Request_Data'])
        # print(resp)
        self.assertEqual(resp, 200)

    @ddt.data(*data[117:118])
    def test2_square_search_is_ok(self, data):
        """ 音乐广场——人名搜索 """
        resp = self.http.post_code(self.lib.api + data['Request_URL'], data=data['Request_Data'])
        # print(resp)
        self.assertEqual(resp, 200)

    @ddt.data(*data[118:119])
    def test3_square_is_ok(self, data):
        """ 音乐广场 """
        resp = self.http.post_code(self.lib.api + data['Request_URL'], data=data['Request_Data'])
        # print(resp)
        self.assertEqual(resp, 200)

    @ddt.data(*data[122:123])
    def test4_activity_detail_is_ok(self, data):
        """ 活动详情 """
        resp = self.http.post_code(self.lib.api + data['Request_URL'], data=data['Request_Data'])
        # print(resp)
        self.assertEqual(resp, 200)

    @ddt.data(*data[124:125])
    def test5_activity_table_is_ok(self, data):
        """ 活动列表——通过类型获取 """
        resp = self.http.post_code(self.lib.api + data['Request_URL'], data=data['Request_Data'])
        # print(resp)
        self.assertEqual(resp, 200)

    @ddt.data(*data[127:128])
    def test6_apply_config_is_ok(self, data):
        """ 报名表单 """
        resp = self.http.post_code(self.lib.api + data['Request_URL'], data=data['Request_Data'])
        # print(resp)
        self.assertEqual(resp, 200)

    @ddt.data(*data[129:130])
    def test7_activity_player_is_ok(self, data):
        """ 报名列表 """
        resp = self.http.post_code(self.lib.api + data['Request_URL'], data=data['Request_Data'])
        # print(resp)
        self.assertEqual(resp, 200)

    @ddt.data(*data[131:132])
    def test8_check_code_is_ok(self, data):
        """ 短信验证码 """
        resp = self.http.post_code(self.lib.url_4 + data['Request_URL'], data=data['Request_Data'])
        # print(resp)
        self.assertEqual(resp, 200)

    @ddt.data(*data[132:133])
    def test9_check_phone_is_ok(self, data):
        """ 手机号唯一性验证 """
        resp = self.http.post_code(self.lib.api + data['Request_URL'], data=data['Request_Data'])
        # print(resp)
        self.assertEqual(resp, 200)

    @ddt.data(*data[133:134])
    def test10_check_name_is_ok(self, data):
        """ 用户名唯一性验证 """

        resp = self.http.post_code(self.lib.api + data['Request_URL'], data=data['Request_Data'])
        # print(resp)
        self.assertEqual(resp, 200)

    @ddt.data(*data[115:116])
    def test11_browse_is_ok(self, data):
        """ 浏览 """
        resp = self.http.post_code(self.lib.api + data['Request_URL'], data=data['Request_Data'])
        # print(resp)
        self.assertEqual(resp, 200)

