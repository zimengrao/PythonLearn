"""
@Name: business
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/11/30
"""

from lib.pc import WebDriver
from config import cnf


class Business(WebDriver):
    def __init__(self):
        super(Business, self).__init__()
        self.config = cnf.Config()
        self.driver = WebDriver()
        self.url = self.config.get_config('HTTP', 'baseurl')

