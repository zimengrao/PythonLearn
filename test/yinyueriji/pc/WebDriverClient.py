"""
@Name: WebDriverClient
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/9
"""

from selenium import webdriver
from lxml.html import fromstring
import time

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

    def switch(self, value):
        self.driver.switch_to.frame(value)

    # def switch_quit(self):
    #     self.driver.switch_to.default_content()
    #
    # def code(self, xpath):
    #     div = self.driver.find_element_by_xpath(xpath)
    #     self.action(self.driver).click_and_hold(on_element=div).perform()
    #     time.sleep(0.15)
    #     self.action(self.driver).move_to_element_with_offset(to_element=div, xoffset=328, yoffset=40).release().perform()

    def check(self, xpath):
        return bool(self.parse(xpath))

    def max_window(self):
        self.driver.maximize_window()


