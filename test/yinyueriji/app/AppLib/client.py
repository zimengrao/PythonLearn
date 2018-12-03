"""
@Name: WebDriverClient
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/10/15
"""

import os
from config.cnf import Config
from appium.webdriver import Remote

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
class Client:
    def __init__(self):
        super(Client, self).__init__()
        self.config = Config()
        self.desired_caps = {
            'platformName' : self.config.get_config('DESIRED_CAPS', 'platformName'),
            'platformVersion': self.config.get_config('DESIRED_CAPS', 'platformVersion'),
            'deviceName': self.config.get_config('DESIRED_CAPS', 'deviceName'),
            'appPackage': self.config.get_config('DESIRED_CAPS', 'appPackage'),
            'appActivity': self.config.get_config('DESIRED_CAPS', 'appActivity'),
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'app': PATH("../Apps/app-release.apk")
        }

        self.driver = Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
        self.driver.implicitly_wait(10)

    def find(self,resource):
        self.driver.find_element_by_id(resource).text()

    def click(self,resource):
        self.driver.find_element_by_id(resource).click()

    def send_keys(self,resource,keywords):
        self.driver.find_element_by_id(resource).send_keys(keywords)

