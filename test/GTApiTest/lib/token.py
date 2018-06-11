"""
@Name: token.py
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/11
"""

import json

from config.readconfig import ReadConfig
from lib.client import HttpHandler

token = None
loginuid = None

class GetToken:
    def __init__(self):
        super(GetToken, self).__init__()
        self.read_config = ReadConfig()
        self.httphandler = HttpHandler()

        self.data_address =self.read_config.get_config('DATABASE', 'data_address')
        self.username = self.read_config.get_config('DATABASE', 'username')
        self.password = self.read_config.get_config('DATABASE', 'password')
        self.login_path = self.read_config.get_config('DATABASE', 'login_path')
        self.url = self.read_config.get_config('HTTP', 'baseurl')
        self.port = self.read_config.get_config('HTTP', 'port')

        self.data = {
            "username": self.username,
            "password": self.password
        }

    def get_token(self):
        ''' 获取登录的token '''
        global token
        global loguid

        resp = json.loads(self.httphandler.post(self.url + self.login_path, data = self.data))
        token = self.httphandler.get_value(resp, 'token')
        loginuid = self.httphandler.get_value(resp, 'userid')

        return token,loginuid

    def set_token(self):
        self.read_config.set_config('DATABASE', token, loginuid)