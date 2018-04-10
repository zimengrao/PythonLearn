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

class GreatToneApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = 'http://m.greattone.net/e/appapi/'
        cls.http = HttpHandler()

    def test_login_is_ok(self):
        """ [GreatTone][login] 接口通过测试"""
        data = {
            'api': 'user/login',
            'username': '贾老师',
            'password': '123456'
        }
        resp = json.loads(self.http.post(self.url, data=data))
        print(json.dumps(resp, indent=4, ensure_ascii=False))
        self.assertEqual(resp.get('info'), '登录成功!')
        self.assertEqual(resp.get('err_msg'), 'success')
        self.assertEqual(self.http.get_value(resp, 'userid'), 48623)
        self.assertEqual(self.http.get_value(resp, 'username'), '贾老师')
        self.assertEqual(self.http.get_value(resp, 'groupid'), '3')

    def test_login_is_null(self):
        """ [GreatTone][login] 用户名和密码为空"""
        data = {
            'api': 'user/login',
        }
        resp = json.loads(self.http.post(self.url, data=data))
        print(resp)
        self.assertEqual(resp.get('err_msg'), 'error')
        self.assertEqual(resp.get('info'), '\u7528\u6237\u540d\u548c\u5bc6\u7801\u4e0d\u80fd\u4e3a\u7a7a')

    def test_login_is_username_null(self):
        """ [GreatTone][login] 用户名和密码为空"""
        data = {
            'api': 'user/login',
            'username': '贾老师'
        }
        resp = json.loads(self.http.post(self.url, data=data))
        print(resp)
        self.assertEqual(resp.get('err_msg'), 'error')
        self.assertEqual(resp.get('info'), '\u7528\u6237\u540d\u548c\u5bc6\u7801\u4e0d\u80fd\u4e3a\u7a7a')
