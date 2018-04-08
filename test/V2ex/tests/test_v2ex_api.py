"""
@Name: test_v2ex_api
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/4/8
"""

import unittest
from lib.client import HttpHandler

class V2exApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.top_url = 'https://www.v2ex.com/api/topics/hot.json'
        cls.show_url = 'https://www.v2ex.com/api/nodes/show.json'
        cls.userinfo_url = 'https://www.v2ex.com/api/members/show.json'
        cls.laster_url = 'https://www.v2ex.com/api/topics/latest.json'
        cls.http =HttpHandler()

    def test_top_api_is_ok(self):
        result = self.http.get(self.top_url)
        for item in result:
            print(self.http.get_value(item, 'title'))
            # self.assertIsNone(self.http.get_value(item, 'title'))
            # base = self.http.get_value(item, 'node')
            # laster_url = self.http.get_value(base, 'name').split('/')[-1]

