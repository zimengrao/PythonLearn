
"""
@Name: test_case_login
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/2/1
"""

import lib # from lib.WebDriverClient import WebDriver
import time
from config import Config
import unittest
from BeautifulReport import BeautifulReport

class TesterHomeCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # self.lib = WebDriver()
        # self.driver = self.lib.driver
        # self.config = Config.enum.get('login')
        # self.url = self.config.get('url')
        # self.username = self.config.get('username')
        # self.password = self.config.get('password')
        # self.input_username, self.input_password, self.click_login_button = self.config.get('xpath')
        # self.assert_info = self.config.get('assert_xpath')[0]

        cls.config = Config.enum.get('login')
        cls.img_path = 'img/'
        cls.url = cls.config.get('url')
        cls.username = cls.config.get('username')
        cls.password = cls.config.get('password')
        cls.input_username, cls.input_password, cls.click_login_button = cls.config.get('xpath')
        cls.assert_info = cls.config.get('assert_xpath')[0]

    def setUp(self):
        # 动态数据构造放到这个方法中
        self.lib = lib.WebDriver()
        self.driver = self.lib.driver

    def tearDown(self):
        self.driver.quit()

    def test_config_enum_is_ok(self):
        # print(self.config)
        # print(self.username)
        # print(self.url)
        # print(self.input_password)
        # assertIsNotNone 存在，pass；对定义的初始值做一些简单的判断

        print('test start with test_config_enum_is_ok')
        self.assertIsNotNone(self.config)
        self.assertIsNotNone(self.username)
        self.assertIsNotNone(self.url)
        self.assertIsNotNone(self.input_password)

    # def test_testerhome_login(self):
    #     self.lib.get(self.url)
    #     self.lib.send_keys(self.input_username, self.username)
    #     self.lib.send_keys(self.input_password, self.password)
    #     self.lib.click(self.click_login_button)
    #     time.sleep(5)
    #     assert_info = self.lib.parse(self.assert_info)[0]
    #     self.assertEqual(assert_info, self.username)
    #
    # @BeautifulReport.add_test_img('testerlife')
    # def test_testerhome_page(self):
    #     self.lib.get('http://testerlife.com')
    #     time.sleep(3)
    #     self.lib.save_img('{}testerlife.png'.format(self.img_path))

    @BeautifulReport.add_test_img('testerlife')
    def test_show_img_in_report(self):
        """展示截图在report.html中"""
        print('测试完成')