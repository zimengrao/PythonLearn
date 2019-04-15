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
import random


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

    def tearDownclass(self):
        self.driver.close_app()
        self.driver.quit()

    def test01_create_video(self):
        ''' 发布视频测试'''
        self.case_name = '发布视频帖'
        self.bus.login()
        self.client.click('com.greattone.greattone:id/tab_rb_2')
        self.client.click('com.greattone.greattone:id/ll_video')
        i = random.randint(1,6)
        content = self.randcs().cre_name()
        while content == None:
            content = self.randcs().cre_name()
        self.client.send_keys('com.greattone.greattone:id/et_content', '第{}个视频'.format(i) + content)
        self.client.click('com.greattone.greattone:id/iv_pic')
        self.client.click("//*[@text='从相册选择视频' and @index='2']")
        self.client.click('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                          'android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.GridView/'
                          'android.widget.FrameLayout[{}]/android.widget.ImageView[2]'.format(i))
        # self.client.click('com.greattone.greattone:id/cb_select_tag')
        self.client.click('com.greattone.greattone:id/btn_ok')
        self.client.click('com.greattone.greattone:id/tv_head_other')
        self.client.click('com.greattone.greattone:id/tab_rb_1')
        self.assertEqual( '第{}个视频'.format(i) + content, self.client.find('//*[@resource-id="com.greattone.greattone:id/adapter_comments_content"]'))

    def test02_creat_photo(self):
        ''' 发布图片测试'''
        self.case_name = '发布图片帖'
        # self.bus.login()
        self.client.click(res='com.greattone.greattone:id/tab_rb_2')
        self.client.click(res='com.greattone.greattone:id/ll_picture')
        content = self.randcs().cre_name()
        while content == None:
            content = self.randcs().cre_name()
        self.client.send_keys('com.greattone.greattone:id/et_content', content)
        self.client.click('com.greattone.greattone:id/iv_pic')
        i = random.randint(1,9)
        t = 1
        print(i)
        while t<i:
            # 选择图片xpath
            self.client.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                'android.widget.RelativeLayout[2]/android.widget.GridView/android.widget.FrameLayout[{}]/android.widget.ImageView[2]'.format(t))
            t = t+1
        self.client.click('com.greattone.greattone:id/btn_ok')
        self.client.click('com.greattone.greattone:id/tv_head_other')
        self.client.click('com.greattone.greattone:id/tab_rb_1')
        self.assertEqual(content, self.client.find('//*[@resource-id="com.greattone.greattone:id/adapter_comments_content"]'))

    def test03_creat_review(self):
        ''' 发布评论测试'''
        self.case_name = '发布评论'
        # self.bus.login()
        self.client.click('com.greattone.greattone:id/tab_rb_1')
        self.client.swipe('com.greattone.greattone:id/adapter_comments_co')
        # self.client.click(res='com.greattone.greattone:id/adapter_comments_co')
        content = self.randcs().cre_name()
        while content == None:
            content = self.randcs().cre_name()
        self.client.send_keys('com.greattone.greattone:id/replay_dialog_edit', content)
        self.client.click('com.greattone.greattone:id/replay_dialog_send')

    def test04_is_like(self):
        ''' 点赞测试'''
        self.case_name = '点赞/取消点赞'
        # self.bus.login()
        self.client.click('com.greattone.greattone:id/tab_rb_1')
        self.client.swipe('com.greattone.greattone:id/adapter_comments_like')
        # self.client.click(res='com.greattone.greattone:id/adapter_comments_co')
        # self.client.click('com.greattone.greattone:id/adapter_comments_like')



