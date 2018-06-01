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

class HqsTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):


        cls.config = Config.enum.get('hqs')
        cls.url = cls.config.get('url')
        cls.login = cls.config.get('login')
        cls.username  = cls.login.get('username')
        cls.password = cls.login.get('password')

        cls.dynamic = cls.config.get('dynamic')
        cls.video_input, cls.video_file = cls.dynamic.get('xpath_video')

        cls.value = cls.dynamic.get('value')
        cls.send = cls.dynamic.get('send')

        cls.assert_url, cls.assert_login = cls.config.get('assert_xpath')

    def setUp(self):
        self.lib = lib.BusinessApi(self.config)
        self.driver = self.lib.driver

    def tearDown(self):
        self.driver.quit()

    def test_hqs_is_ok(self):
        ''' 好琴声网站 is ok'''
        self.lib.get(self.url)
        self.assertIn(self.url, self.lib.parse(self.assert_url)[0])

    def test_config_enum_is_ok(self):
        '''判断参数不为空'''
        self.assertIsNotNone(self.config)
        self.assertIsNotNone(self.username)
        self.assertIsNotNone(self.password)

    def test_login_is_ok(self):
        '''login is ok'''
        self.lib.hqs_login()
        self.assertEqual('退出', self.lib.parse(self.assert_login)[0])

    def test_video_is_ok(self):
        self.lib.hqs_dynamic()
        self.lib.send_keys(self.video_input, self.video_file)
        time.sleep(5)
        self.lib.send_keys(self.video_input, self.video_file)
        self.lib.click(self.send)





