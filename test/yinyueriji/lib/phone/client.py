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
            'autoGrantPermissions': True,
            'automationName': 'uiautomator2',
            'app': PATH("packages/apps-release.apk")
        }
        self.driver_url = self.config.get_config('APP_DATABASE','driver_url')
        # self.driver = Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
        self.driver = Remote('{}'.format(self.driver_url), self.desired_caps)
        self.driver.implicitly_wait(15)

    def find(self,xpath):
        result=self.driver.find_element_by_xpath(xpath).text
        return result

    def click(self,res):
        try:
            self.driver.find_element_by_id(res).click()
        except:
            self.driver.find_element_by_xpath(res).click()

    def xpath(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def send_keys(self,res,keywords):
        try:
            self.driver.find_element_by_id(res).send_keys(keywords)
        except:
            self.driver.find_element_by_xpath(res).send_keys(keywords)

    def swipe(self, res):
        width = self.driver.get_window_rect()['width']
        height = self.driver.get_window_rect()['height']
        i = 0
        while i<10:
            try:
                self.driver.find_element_by_id(res).click()
                break
            except Exception as e:
                self.driver.swipe(width/2,height*0.8,width/2,height*0.2)
                i = i +1

    def isElemnet(self):
        self.driver.is


