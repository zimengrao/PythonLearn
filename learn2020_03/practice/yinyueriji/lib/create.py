"""
@Name: create
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2019/4/17
"""

"""
@Name: business
@Version:
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/9
"""

import ast
import collections
import json
import random

from lib.web.client import HttpHandler
from config.ReadExcel import ExcelData
# from config.WriteExcel import WriteData
from config.cnf import Config
from config.mysql import MysqlData


# get_user = ExcelData('user').readData()

class BusinessApi(HttpHandler):
    def __init__(self):
        super(BusinessApi, self).__init__()
        self.http = HttpHandler()
        self.config = Config()
        self.read = ExcelData
        self.mysql = MysqlData()

        self.url = self.config.get_config('HTTP', 'baseurl')  # 4.0PC网站地址
        self.appapi_url = self.config.get_config('HTTP', 'appapi')  # 4.0-appapi接口地址
        self.webapi_url = self.config.get_config('HTTP', 'webapi')  # 4.0-webapi接口地址
        self.username = self.config.get_config('DATABASE', 'username')
        self.password = self.config.get_config('DATABASE', 'password')
        self.login_path = self.config.get_config('DATABASE', 'login_path')  # 登录接口API

        self.data_address = self.config.get_config('DATABASE', 'data_address')
        self.port = self.config.get_config('HTTP', 'port')

        self.post_data = {
            "cmd": "login",
            "params":
                {
                    "login_type": "a7d3bbc5-dcb7-53ff-2df1-af203a832b52",
                    "account": self.username,
                    "password": self.password,
                    "openid": ""
                }
        }

    def get_token(self):
        ''' 获取登录的token 并更新配置文件config.ini token和loginuid数据'''

        # print(self.post_data)
        # print(self.url_4 + self.login_path)
        post_data = json.dumps(self.post_data)
        resp = json.loads(self.http.post(self.webapi_url + self.login_path, data=post_data))
        # print(resp)
        if self.get_value(resp, 'info') == '登录成功！':
            token_data = str(self.http.get_value(resp, 'logintoken'))
            loginuid_data = str(self.http.get_value(resp, 'loginuid'))
            self.config.set_config('DATABASE', 'token', token_data)
            self.config.set_config('DATABASE', 'loginuid', loginuid_data)
            return loginuid_data, token_data
        else:
            print('登录失败或接口错误')

    def create_activity_haixuan(self):
        '''

        :return: 用户登录
        '''

        data = self.read.get_config('create_appapi')
        print(data)
        select_data = "SELECT tc002_name, tc002_login_token from gt002_user_auth where tc002_name = %s" % ''

