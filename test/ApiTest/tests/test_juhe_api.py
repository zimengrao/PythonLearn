"""
@Name: test
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/18
"""

import unittest
import json
import requests
from lib.client import HttpHandler
from lxml import etree
import config

class TesterHome(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http = HttpHandler()
        cls.url = 'http://apis.juhe.cn/cook/query'
        cls.data = {
            'menu': '鱼香肉丝',
            'key': '338ce1ecb756bf7ca4772fbb9f11cd75',
        }

    def test_api_is_ok(self):
        """[API][菜谱] 测试聚合菜谱返回的结果正确"""
        response = self.http.post(self.url, data=self.data)
        base_info = self.http.get_value(response, 'data')
        for info in base_info:
            self.assertEqual(self.data['menu'] in self.http.get_value(info, 'title'), True)

    def test_post_method_is_ok(self):
        """[API][菜谱] 测试聚合post请求返回结果正确"""
        url = 'http://v.juhe.cn/weixin/query'
        data = dict(
            key='4beb9d77d2b95ce9bec6d8363ee5a620'
        )
        response = self.http.post(url, data=data)
        infos = self.http.get_value(response, 'list')
        self.assertEqual(len(infos), 20)
        for info in infos:
            self.assertEqual(self.http.valid_json(info, 'juhe', 'wechat_search_schema'), True)
            # self.assertEqual(self.http.get_value(info, 'id').split[0:8], '1521366')
            print('='*50)