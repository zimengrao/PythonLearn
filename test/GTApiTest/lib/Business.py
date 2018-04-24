"""
@Name: Business
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/4/10
"""

from .client import HttpHandler
from config import Config
import json

class BusinessApi(HttpHandler):
    def __init__(self):
        super(BusinessApi, self).__init__()

        self.config = Config.enum.get('GTApi')
        self.base_url = self.config.get('base_url')

        self.data_null = self.config.get('login')[0]
        self.data_password_null = self.config.get('login')[1]
        self.data_username_null = self.config.get('login')[2]
        self.data_password_false = self.config.get('login')[3]
        self.data_true = self.config.get('login')[4]

        self.guang_url = self.config.get('guangchang').get('guang_url')
        self.guang, self.tuijian, self.nian, self.ji, self.zhou = self.config.get('guangchang').get('value')

    def login(self, data=None):
        resp = json.loads(self.post(self.base_url, data=data))

        print(json.dumps(resp, indent=4, ensure_ascii=False))
        return resp

    # def login_value(self):
    #     resp = json.loads(self.post(self.base_url, data=self.data_true))
    #     print(json.dumps(resp, indent=4, ensure_ascii=False))
    #     token = self.get_value(resp, 'token')
    #     loginuid = self.get_value(resp, 'loginuid')
    #     return [token, loginuid]