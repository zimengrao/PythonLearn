"""
@Name: test_dynamic_apply
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/11
"""

import unittest
# from lib.client import  HttpHandler
# from config.config import Config
from lib.token import GetToken


class DynamicApply(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.http = HttpHandler()
        # cls.config = Config()
        cls.token = GetToken()

    def test_login_is_ok(self):
        self.token.get_token()