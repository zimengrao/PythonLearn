"""
@Name: BusinessApi
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/15
"""

from lib.WebDriverClient import WebDriver
import time
import os

class BusinessApi(WebDriver):
    def __init__(self, config):
        super(BusinessApi, self).__init__()

        self.config = config
        self.url = self.config.get('url')
        self.login = self.config.get('login')
        self.username = self.login.get('username')
        self.password = self.login.get('password')
        self.click_login_button1, self.input_username, self.input_password, \
            self.click_login_button2 = self.login.get('xpath_login')

        self.dynamic = self.config.get('dynamic')
        self.guangchang, self.fatie_xpath = self.dynamic.get('xpath_dynamic')

        self.click_video, self.click_music, self.click_photo = self.dynamic.get('click_dynamic')

    def hqs_login(self):
        self.get(self.url)
        self.click(self.click_login_button1)
        time.sleep(0.5)
        self.send_keys(self.input_username, self.username)
        self.send_keys(self.input_password, self.password)
        self.click(self.click_login_button2)
        time.sleep(4)

    def hqs_guangchang(self):
        ''' 从音乐广场 点击到发帖界面'''
        self.hqs_login()
        self.click(self.guangchang)
        self.click(self.fatie_xpath)
        time.sleep(3)

    def hqs_uploads(self,file):
        os.system("upload.exe %s" %file)


