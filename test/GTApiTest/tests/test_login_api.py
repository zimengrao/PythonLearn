"""
@Name: test_login_api
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/4/10
"""
import unittest
from lib.client import HttpHandler
from lib.business import BusinessApi

class LoginApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
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
        global token
        global loginuid


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
