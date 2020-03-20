"""
@Name: test_douban_api
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/18
"""

import json
import unittest
from lib.client import HttpHandler
import config

class TestDouBaiApi(unittest.TestCase):
    http = None

    @classmethod
    def setUpClass(cls):
        cls.http = HttpHandler()
        cls.base_config = config.Config.enum.get('douban')
        cls.search_url = cls.base_config.get('search_url')

    @classmethod
    def tearDown(cls):
        cls.http.session.close()

    def test_douban_search(self):
        """[豆瓣][API]测试豆瓣读书接口，查询三国演义调用正常"""
        keyword = '?q=三国演义'
        url = self.search_url + keyword
        response = self.http.get(url)
        assert_original_title = self.http.get_value(response, 'original_title')
        self.assertEquals(assert_original_title, '三国演义')

    def test_douban_read(self):
        """[豆瓣][API] 测试豆瓣图书接口，查询tag返回的内容并对解析结果进行断言"""
        keyword = '?tag=青年'
        url = self.search_url + keyword
        response = self.http.get(url)
        # print(json.dumps(response, indent=4, ensure_ascii=False))
        infos = self.http.get_value(response, 'books')

        for info in infos:
            self.assertIsNotNone(self.http.get_value(info, 'series'))

    def test_resursion_list_for_key_to_dict(self):
        """[LIB][方法测试] 测试Recursion.list_for_key_to_dict方法返回正确"""
        data = {
            'a': 1,
            'b': 2,
            'c': {
                'd': 3,
                'e': 4,
                'f': [
                    {1: 2},
                    {1: 2},
                    {1: 2}
                ]
            }
        }

        # assert_info = self.http.get_value(data, 'f')
        # for value in assert_info:
        #     self.assertEqual(self.http.get_value(value, 1), 2)
        data = self.http.list_for_key_to_dict('a', 'c', 'e', my_dict=data)
        self.assertEqual(len(data), 3)

    def test_resursion_get_value(self):
        """[LIB][方法测试] 测试Recursion.get_value方法返回正确"""
        data = {
            'a': 1,
            'b': 2,
            'c': {
                'd': 3,
                'e': 4,
                'f': [
                    {1: 2},
                    {1: 2},
                    {1: 2}
                ]
            }
        }

        assert_info = self.http.get_value(data, 'f')
        for value in assert_info:
            self.assertEqual(self.http.get_value(value, 1), 2)