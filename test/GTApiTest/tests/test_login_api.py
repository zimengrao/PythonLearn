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

class GreatToneApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = Config.enum.get('GTApi')
        cls.url = cls.config.get('base_url')
        cls.data = cls.config.get('login')
        cls.http = HttpHandler()

    def test_login_is_ok(self):
        """ [GreatTone][login] 正确的用户名、密码"""
        resp = json.loads(self.http.post(self.url, data=self.data))
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
        self.assertEqual(resp.get('info'), '用户名和密码不能为空')

    def test_login_is_username_null(self):
        """ [GreatTone][login] 用户名填写，密码为空"""
        data = {
            'api': 'user/login',
            'username': '读后感客户端上老师'
        }
        resp = json.loads(self.http.post(self.url, data=data))
        print(resp)
        self.assertEqual(resp.get('err_msg'), 'error')
        self.assertEqual(resp.get('info'), '用户名和密码不能为空')

    def test_login_password_false(self):
        """ [GreatTone][login] 用户名填写，密码为空"""
        data = {
            'api': 'user/login',
            'username': '贾老师',
            'password': '565699'
        }
        resp = json.loads(self.http.post(self.url, data=data))
        print(resp)
        self.assertEqual(resp.get('err_msg'), 'error')
        self.assertEqual(resp.get('info'), '您的用户名或密码有误!')
