"""
@Name: WebDriverClient
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/2/1
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
        html = self.driver.page_source
        return fromstring(html).xpath(xpath)

    def click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def send_keys(self, xpath, value):
        self.driver.find_element_by_xpath(xpath).send_keys(value)

    def check_elements(self, xpath):
        return bool(self.driver.find_element_by_xpath(xpath))

    def save_img(self, img_name, path='.'):
        self.driver.get_screenshot_as_file(path + img_name)