"""
@Name: test
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/13
"""
import lib
import time
import unittest
from config import Config
from BeautifulReport import  BeautifulReport

class HqsTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = Config.enum.get('login')
        cls.url = cls.config.get('url')
        cls.username  = cls.config.get('username')
        cls.password = cls.config.get('password')
        cls.click_login_button1, cls.input_username, cls.input_password, cls.click_login_button2 = cls.config.get('xpath')
        cls.url_login = cls.config.get('url_login')
        cls.assert_info = cls.config.get('assert_xpath')

    def setUp(self):
        self.lib = lib.WebDriver()
        self.driver = self.lib.driver

    def tearDown(self):
        self.driver.quit()

    def test_config_enum_is_ok(self):
        self.assertIsNotNone(self.config)
        self.assertIsNotNone(self.url)
        self.assertIsNotNone(self.password)

    def test_hqs_login(self):
        self.lib.get(self.url)
        self.lib.click(self.click_login_button1)
        self.lib.send_keys(self.input_username, self.username)
        self.lib.send_keys(self.input_password, self.password)
        self.lib.click(self.click_login_button2)
        time.sleep(2)
        self.lib.get(self.url_login)
        time.sleep(2)
        self.assert_info =self.lib.parse(self.assert_info)




