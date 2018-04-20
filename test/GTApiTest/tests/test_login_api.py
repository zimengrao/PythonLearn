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
        cls.data, cls.data1, cls.data2, cls.data3 = cls.config.get('login')[4], \
                                                    cls.config.get('login')[0], \
                                                    cls.config.get('login')[0], \
                                                    cls.config.get('login')[3]

        cls.guangchang_url = cls.config.get('guangchang')
        cls.http = HttpHandler()


    def test_login_is_ok(self):
        """ [GreatTone][login] 正确的用户名、密码"""
        # data = {
        #     'api': 'user/login',  # 错误的用户名，错误的密码
        #     'username': '贾老师',
        #     'password': '123456'
        # }
        resp = json.loads(self.http.post(self.url, data=self.data))
        print(json.dumps(resp, indent=4, ensure_ascii=False))
        self.assertEqual(resp.get('info'), '登录成功!')
        self.assertEqual(resp.get('err_msg'), 'success')
        self.assertEqual(self.http.get_value(resp, 'userid'), 48623)
        self.assertEqual(self.http.get_value(resp, 'username'), '贾老师')
        self.assertEqual(self.http.get_value(resp, 'groupid'), '3')

    def test_login_is_null(self):
        """ [GreatTone][login] 用户名和密码为空"""
        # data = {
        #     'api': 'user/login',
        # }
        resp = json.loads(self.http.post(self.url, data=self.data1))
        print(resp)
        self.assertEqual(resp.get('err_msg'), 'error')
        self.assertEqual(resp.get('info'), '用户名和密码不能为空')

    def test_login_is_username_null(self):
        """ [GreatTone][login] 用户名填写，密码为空"""
        # data = {
        #     'api': 'user/login',
        #     'username': '读后感客户端上老师'
        # }
        resp = json.loads(self.http.post(self.url, data=self.data2))
        print(resp)
        self.assertEqual(resp.get('err_msg'), 'error')
        self.assertEqual(resp.get('info'), '用户名和密码不能为空')

    def test_login_password_false(self):
        """ [GreatTone][login] 用户名正确，密码错误"""
        # data = {
        #     'api': 'user/login',
        #     'username': '贾老师',
        #     'password': '565699'
        # }
        resp = json.loads(self.http.post(self.url, data=self.data3))
        print(resp)
        self.assertEqual(resp.get('err_msg'), 'error')
        self.assertEqual(resp.get('info'), '您的用户名或密码有误!')

    def test_guangchang_is_ok(self):
        """ [GreatTone][guangchang] is ok"""
        resp = json.loads(self.http.post(self.url, data=self.data))
        token = self.http.get_value(resp, 'token')
        loginuid = self.http.get_value(resp, 'userid')
        self.url = self.url + self.guangchang_url.format(1, loginuid, token)
        resp = json.loads(self.http.get(self.url))
        print(json.dumps(resp, indent=4, ensure_ascii=False))

        self.assertEqual(resp.get('website'), 'http://test.greattone.net')
        self.assertEqual(resp.get('total'), '13911')
        self.assertEqual(resp.get('pageSize'), 10)
        self.assertEqual(resp.get('info'), '读取信息列表成功')
        self.assertEqual(resp.get('err_msg'), 'success')
        self.assertEqual(resp.get('classid'), 1)

        print(resp)
        data = self.http.get_value(resp, 'data')
        for item in data:
            self.assertEqual(self.http.valid_json(item, 'haoqinsheng', 'guangchang'), True)
