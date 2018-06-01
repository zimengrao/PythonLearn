"""
@Name: WebDriverClient
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/9
"""

from selenium import webdriver
from lxml.html import fromstring
from selenium.webdriver.support.select import Select


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
