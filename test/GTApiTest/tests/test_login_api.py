"""
@Name: test_login_api
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/4/10
"""
import json
import unittest
from lib.client import HttpHandler
from config import Config
from lib.business import BusinessApi

class GreatToneApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = Config.enum.get('GTApi')
        cls.url = cls.config.get('base_url')
        cls.http = HttpHandler()
        cls.lib = BusinessApi()

    def test_login_is_ok(self):
        """ [GreatTone][login] 正确的用户名、密码"""

        resp = self.lib.login(self.lib .data_true)
        self.assertEqual(resp.get('info'), '登录成功!')
        self.assertEqual(resp.get('err_msg'), 'success')
        self.assertEqual(self.http.get_value(resp, 'userid'), 48623)
        self.assertEqual(self.http.get_value(resp, 'username'), '贾老师')
        self.assertEqual(self.http.get_value(resp, 'groupid'), '3')

    def test_login_is_null(self):
        """ [GreatTone][login] 用户名和密码为空"""

        resp = self.lib.login(self.lib.data_null)
        self.assertEqual(resp.get('err_msg'), 'error')
        self.assertEqual(resp.get('info'), '用户名和密码不能为空')

    def test_login_is_username_null(self):
        """ [GreatTone][login] 用户名填写，密码为空"""

        resp = self.lib.login(self.lib.data_username_null)
        self.assertEqual(resp.get('err_msg'), 'error')
        self.assertEqual(resp.get('info'), '用户名和密码不能为空')

    def test_login_password_false(self):
        """ [GreatTone][login] 用户名正确，密码错误"""

        resp = self.lib.login(self.lib.data_password_false)
        self.assertEqual(resp.get('err_msg'), 'error')
        self.assertEqual(resp.get('info'), '您的用户名或密码有误!')
    #
    # def test_guangchang_api_is_ok(self):
    #     """ [GreatTone][guangchang] api is ok"""
    #     self.url = self.lib.base_url + self.lib.guang_url + \
    #                self.lib.guang.format(10, self.lib.login_value()[0], self.lib.login_value()[1])
    #     resp = json.loads(self.http.get(self.url))
    #     print(json.dumps(resp, indent=4, ensure_ascii=False))
    #
    #     self.assertEqual(resp.get('website'), 'http://test.greattone.net')
    #     self.assertEqual(resp.get('total'), '13911')
    #     self.assertEqual(resp.get('pageSize'), 10)
    #     self.assertEqual(resp.get('info'), '读取信息列表成功')
    #     self.assertEqual(resp.get('err_msg'), 'success')
    #     self.assertEqual(resp.get('classid'), 1)
    #
    #     data = self.http.get_value(resp, 'data')
    #     for item in data:
    #         self.assertEqual(self.http.valid_json(item, 'haoqinsheng', 'guangchang'), True)
