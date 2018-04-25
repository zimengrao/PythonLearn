"""
@Name: test_guangchang_api.py
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/4/20
"""

import json
import unittest
from lib.client import HttpHandler
from lib.business import BusinessApi

class GangApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.http = HttpHandler()
        cls.lib = BusinessApi()

    def test_guang_api_is_ok(self):
        """ [GreatTone][guang] api is ok 音乐广场接口测试"""

        i = 0
        self.lib.login_value()
        for item in self.lib.value:

            resp = self.lib.guangchang_url(item)
            self.assertEqual(resp.get('website'), self.lib.homepage)
            # self.assertEqual(resp.get('total'), '15070')
            self.assertEqual(resp.get('pageSize'), 1)
            self.assertEqual(resp.get('info'), '读取信息列表成功！')
            self.assertEqual(resp.get('err_msg'), 'success')
            self.assertEqual(resp.get('classid'), '1')

            data = self.http.get_value(resp, 'data')
            for item in data:
                self.assertEqual(self.http.valid_json(item, 'haoqinsheng', 'guangchang'), True)

            i += 1
            print('第{}次测试完成'.format(i))

        def test_guanzhu_api_is_ok(self):
            """ [GreatTone][guanzhu] api is ok 音乐广场接口测试"""


