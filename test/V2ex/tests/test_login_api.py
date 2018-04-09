"""
@Name: test_login_api
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/4/9
"""

import json
import unittest

from lib.client import HttpHandler

class V2exApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = 'http://m.greattone.net/e/appapi/'
        cls.http = HttpHandler()

    def test_login_is_ok(self):

        data = {
            'api': 'user/login',
            'username': '贾老师',
            'password': '123456'
        }

        response = self.http.post(self.url, data=data)
        print(response)