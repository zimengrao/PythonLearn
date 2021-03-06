"""
@Name: tests_iqiyi
@Version:
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/10
"""

"""
@Name: test_baidu
@Version:
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/10
"""

import unittest
from lib.WebDriverClient import WebDriver
from config import Config

class TestIQiYi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = Config.enum
        cls.iqiyi_url = cls.config.get('iqiyi').get('home_page')
        cls.iqiyi_element = cls.config.get('iqiyi').get('xpath')[0]
        cls.iqiyi_assert = cls.config.get('iqiyi').get('assert_xpath')[0]

    def setUp(self):
        self.lib = WebDriver()
        self.driver = self.lib.driver

    def tearDown(self):
        # 关闭浏览器
        # self.driver.close() 关闭浏览器table页面
        self.driver.quit()

    def test_iqiyi_home_page(self):
        assert_name = '电影频道-热门好看的电影大全-正版高清电影在线观看-爱奇艺'
        self.lib.get(self.iqiyi_url)
        self.lib.click(self.iqiyi_element)
        self.assertEqual(self.lib.parse(self.iqiyi_assert)[0], assert_name)