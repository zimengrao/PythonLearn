"""
@Name: WebDriverCllient.py
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/8
"""

from selenium import webdriver
from lxml.html import fromstring

class WebDriver:
    def __init__(self):

        self.driver = self.init_driver()

    def init_driver(self):
        return webdriver.Firefox()

    def get(self, url):
        self.driver.get(url)

    def parse(self, xpath):
        return fromstring(self.driver.page_source).xpath(xpath)

    def click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def send_keys(self, xpath, value):
        self.driver.find_element_by_xpath(xpath).send_keys(value)

    def check(self, xpath):
        return bool(self.parse(xpath))

    # def switch_tabs(self):
    #     # 当前窗口
    #     now_handel = self.driver.current_window_handle
    #     handlers = self.driver.window_handles
    #     for handler in handlers:
    #         if handler != now_handel:
    #             self.driver.switch_to_window(handler)
