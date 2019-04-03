"""
@Name: AppBusiness
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/10/15
"""

from config.cnf import Config
from lib.phone.client import Client

class AppBusiness(Client):
    def __init__(self):
        super(Client, self).__init__()
        self.config = Config()
        self.client = Client()

        self.username = self.config.get_config('DATABASE', 'username')
        self.password = self.config.get_config('DATABASE', 'password')

        # self.driver = self.client.driver
    def login(self):
        self.client.send_keys('com.greattone.greattone:id/et_name', u'艾丹特纳')
        self.client.send_keys('com.greattone.greattone:id/et_password', '123456')
        self.client.click('com.greattone.greattone:id/btn_sign_in')
        # self.client.click('com.android.packageinstaller:id/permission_allow_button')



