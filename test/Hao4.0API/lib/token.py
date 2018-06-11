"""
@Name: token
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/11
"""

import json

from config.config import Config
from lib.client import HttpHandler

token = None
loginuid = None

class GetToken:
    def __init__(self):
        super(GetToken, self).__init__()
        self.config = Config()
        self.http = HttpHandler()

        self.data_address =self.config.get_config('DATABASE', 'data_address')
        self.username = self.config.get_config('DATABASE', 'username')
        self.password = self.config.get_config('DATABASE', 'password')
        self.login_path = self.config.get_config('DATABASE', 'login_path')
        self.url = self.config.get_config('HTTP', 'baseurl')
        self.port = self.config.get_config('HTTP', 'port')

        self.data = {
            'api': self.login_path,
            'username': self.username,
            'password': self.password
        }

    def get_token(self):
        ''' 获取登录的token '''
        global token
        global loguid

        resp = json.loads(self.http.post(self.url, data = self.data))
        token = self.http.get_value(resp, 'token')
        loginuid = self.http.get_value(resp, 'userid')

        return token,loginuid

    def set_token(self):

        self.get_token()
        self.config.set_config('DATABASE', self.get_token()[0], self.get_token()[1])