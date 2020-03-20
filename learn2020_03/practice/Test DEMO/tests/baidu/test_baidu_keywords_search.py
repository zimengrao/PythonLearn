
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

    def setUp(self):
        # 动态数据构造放到这个方法中
        self.lib = lib.BusinessApi(self.config)
        self.driver = self.lib.driver

    def tearDown(self):
        self.driver.quit()

    def test_config_enum_is_ok(self):
        """[百度][Config] 验证百度config文件是否正确"""
        print('test start with test_config_enum_is_ok')
        self.assertIsNotNone(self.lib.config)
        self.assertIsNotNone(self.lib.keywords)
        self.assertIsNotNone(self.lib.url)
        self.assertIsNotNone(self.lib.assert_title)
        self.assertIsNotNone(self.lib.assert_tieba_title)
        print('断言所有配置')

    def test_baidu_search_is_ok(self):
        """[百度][TEST] 在百度首页输入搜索关键字，确认返回结果正确"""
        self.lib.baidu_search(self.lib.url, self.lib.keywords)
        self.assertIsNotNone(self.lib.parse(self.lib.assert_title))
        self.assertEqual(self.lib.parse(self.lib.assert_title)[0], '{}_百度搜索'.format(self.lib.keywords))

    @BeautifulReport.add_test_img('test')
    def test_baidu_tieba(self):
        """[百度][TEST] 测试搜索后，跳转到贴吧中的title与预期结果一致"""
        print('在百度搜索中输入{}关键字进行查询并跳转到查询结果页面')
        self.lib.baidu_search(self.lib.url, self.lib.keywords)
        self.lib.driver.get_screenshot_as_file('img/test.png')
        self.lib.click(self.lib.tieba_button)
        self.assertEqual(str(self.lib.parse(self.lib.assert_tieba_title)[0]).strip(), '淘宝网吧')