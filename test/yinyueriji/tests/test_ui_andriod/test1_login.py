"""
@Name: test_login
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/10/15
"""

import unittest
# from lib.phone.client import Client
from lib.phone.AppBusiness import AppBusiness


# global driver
# data= ExcelData('andriod').readData()

# @ddt.ddt
class AndriodUiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.client = Client()
        # cls.driver = cls.client.driver
        cls.bus = AppBusiness()
        cls.client = cls.bus.client
        cls.driver = cls.bus.client.driver

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

    def test01_login_is_ok(self):
        '''用户名密码正确，登录成功'''
        # time.sleep(10)
        self.case_name = '输入正确的用户名密码，登录成功'
        self.client.send_keys('com.greattone.greattone:id/et_name',u'艾丹特纳')
        self.client.send_keys('com.greattone.greattone:id/et_password','123456')
        self.client.click('com.greattone.greattone:id/btn_sign_in')
        # self.assertEqual(self.appLib.find('com.greattone.greattone:id/tab_rb_3'), '我的')
        # time.sleep(10)

    def test02_creat_video(self):
        ''' 发布视频'''
        self.case_name = '发布视频'
        # self.bus.login()


