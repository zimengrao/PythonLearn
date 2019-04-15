"""
@Name: test1_create
@Version:
@Project: PyCharm
@Author: wangmin
@Data: 2019/3/27
"""
import unittest
# from lib.app.client import Client
from lib.phone.AppBusiness import AppBusiness
from config.RandomChinese import Random_Chinese
import time


# global driver
# data= ExcelData('andriod').readData()

# @ddt.ddt
class AndriodTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.bus = AppBusiness()
        cls.client = cls.bus.client
        cls.driver = cls.bus.client.driver
        cls.randcs = Random_Chinese

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

    def test01_square(self):
        ''' 发布视频测试'''
        self.case_name = '发布视频'
        self.bus.login()
        # self.client.click(res='com.greattone.greattone:id/adapter_comments_content')
        te=self.client.find('//*[@resource-id="com.greattone.greattone:id/adapter_comments_content"]')
        self.assertEqual(te,'垣驰汤膨豫绪')
        print(te)

        # print(ddd)
        # if content==self.client.find('com.greattone.greattone:id/adapter_comments_content'):
        #     return True
        # else:
        #     return False
        # self.driver.tap([30,1676],[1049,1809])
        # self.driver.tap([253,236],[343,326])
        # self.client.click('com.greattone.greattone:id/tv_head_other')
        time.sleep(10)

    # def test02_creat_video(self):
    #     ''' 发布视频'''
    #     self.case_name = '发布视频'
    #     # self.bus.login()


