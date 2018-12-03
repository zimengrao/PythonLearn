"""
@Name: test_login
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/10/15
"""

import unittest
from app.AppLib.client import Client


# global driver
# data= ExcelData('andriod').readData()

# @ddt.ddt
class AndriodTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.appLib = Client()
        cls.driver = cls.appLib.driver

    # def setUp(self):
    #     self.appLib = AppBusiness()
    #     self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.appLib.desired_caps)
    #     self.driver.implicitly_wait(10)
    #
    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

    def test01_login_is_ok(self):
        '''用户名密码正确，登录成功'''
        # time.sleep(10)
        self.appLib.send_keys('com.greattone.greattone:id/et_name',u'艾丹特纳')
        self.appLib.send_keys('com.greattone.greattone:id/et_password','123456')
        self.appLib.click('com.greattone.greattone:id/btn_sign_in')
        # print(self.appLib.find('com.greattone.greattone:id/tab_rb_3'))
        # self.assertEqual(self.appLib.find('com.greattone.greattone:id/tab_rb_3'), '我的')
        # time.sleep(10)

    # def test02_
