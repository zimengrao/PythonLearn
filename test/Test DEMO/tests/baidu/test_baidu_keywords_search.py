
"""
@Name: test_baidu_keyword
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/5
"""
import lib # from lib.WebDriverClient import WebDriver
import os
import time
from config import Config
import unittest
from BeautifulReport import BeautifulReport

class BaiDuTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = Config.enum.get('baidu')
        cls.img_path = 'img/'
        cls.url = cls.config.get('url')
        cls.keywords = cls.config.get('keywords')
        cls.search_input_element, cls.click_search_button, cls.tieba_button = \
            cls.config.get('xpath')
        cls.assert_title, cls.assert_tieba_title = cls.config.get('assert_xpath')

    def setUp(self):
        # 动态数据构造放到这个方法中
        self.lib = lib.WebDriver()
        self.driver = self.lib.driver

    def tearDown(self):
        self.driver.quit()

    def test_config_enum_is_ok(self):
        """[百度][Config] 验证百度config文件是否正确"""
        print('test start with test_config_enum_is_ok')
        self.assertIsNotNone(self.config)
        self.assertIsNotNone(self.keywords)
        self.assertIsNotNone(self.url)
        self.assertIsNotNone(self.assert_title)
        self.assertIsNotNone(self.assert_tieba_title)

    def test_baidu_search_is_ok(self):
        """[百度][TEST] 在百度首页输入搜索关键字，确认返回结果正确"""
        self.lib.get(self.url)
        self.lib.send_keys(self.search_input_element, self.keywords)
        self.lib.click(self.click_search_button)
        time.sleep(1)
        self.assertIsNotNone(self.lib.parse(self.assert_title))
        self.assertEqual(self.lib.parse(self.assert_title)[0], '{}_百度搜索'.format(self.keywords))

    def test_baidu_tieba(self):
        """[百度][TEST] 测试搜索后，跳转到贴吧中的title与预期结果一致"""
        self.lib.get(self.url)
        self.lib.send_keys(self.search_input_element, self.keywords)
        self.lib.click(self.click_search_button)
        time.sleep(1)
        self.lib.click(self.tieba_button)
        self.assertEqual(str(self.lib.parse(self.assert_tieba_title)[0]).strip(), '淘宝网吧')