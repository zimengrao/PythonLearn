"""
@Name: BusnessClass
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/6
"""
import time
from .WebDriverClient import WebDriver

class BusinessApi(WebDriver):
    """"""
    def __init__(self, config):
        super(BusinessApi, self).__init__()
        self.config = config
        self.img_path = 'img/'
        print(self.img_path)
        self.url = self.config.get('url')
        self.keywords = self.config.get('keywords')
        self.search_input_element, self.click_search_button, self.tieba_button = \
            self.config.get('xpath')
        self.assert_title, self.assert_tieba_title = self.config.get('assert_xpath')

    def baidu_search(self, url, keywords):
        self.get(url)
        self.send_keys(self.search_input_element, self.keywords)
        self.click(self.click_search_button)
        time.sleep(1)


