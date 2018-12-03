"""
@Name: data
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/7/17
"""

from config.mysql import MysqlData
from lib.client import HttpHandler
from config.cnf import Config
import json

class UserData(HttpHandler):
    def __init__(self):
        super(UserData, self).__init__()
        self.mysql = MysqlData()
        self.http = HttpHandler()
        self.config = Config()
        self.url_4 = self.config.get_config('HTTP', 'baseurl_dev') # 4.0接口地址
        self.login_path = self.config.get_config('DATABASE', 'login_path') # 登录接口API

    def normal(self):
        '''
        爱乐人
        :return: 用户id和token
        '''
        post_data = {
            "cmd": "login",
            "params":
                {
                        "login_type": "a7d3bbc5-dcb7-53ff-2df1-af203a832b52",
                        "account": "qingqing",
                        "password": "123456",
                        "openid": ""
                 }
        }
        post_data = json.dumps(post_data)
        result = json.loads(self.http.post(self.url_4 + self.login_path, data=post_data))
        return self.http.get_value(result, 'loginuid'),self.http.get_value(result, 'logintoken')

    def unteacher(self):
        '''
        未认证老师
        :return: 用户id和token
        '''
        post_data = {
            "cmd": "login",
            "params":
                {
                        "login_type": "a7d3bbc5-dcb7-53ff-2df1-af203a832b52",
                        "account": "苏丹",
                        "password": "123456",
                        "openid": ""
                 }
        }
        post_data = json.dumps(post_data)
        result = json.loads(self.http.post(self.url_4 + self.login_path, data=post_data))
        return self.http.get_value(result, 'loginuid'), self.http.get_value(result, 'logintoken')

    def teacher(self):
        '''
        已认证老师
        :return: 用户id和token
        '''
        post_data = {
            "cmd": "login",
            "params":
                {
                        "login_type": "a7d3bbc5-dcb7-53ff-2df1-af203a832b52",
                        "account": "张芳",
                        "password": "123456",
                        "openid": ""
                 }
        }
        post_data = json.dumps(post_data)
        result = json.loads(self.http.post(self.url_4 + self.login_path, data=post_data))
        return self.http.get_value(result, 'loginuid'), self.http.get_value(result, 'logintoken')

    def unstore(self):
        '''
        未认证琴行
        :return: 用户id和token
        '''
        post_data = {
            "cmd": "login",
            "params":
                {
                        "login_type": "a7d3bbc5-dcb7-53ff-2df1-af203a832b52",
                        "account": "维也纳钢琴",
                        "password": "123456",
                        "openid": ""
                 }
        }
        post_data = json.dumps(post_data)
        result = json.loads(self.http.post(self.url_4 + self.login_path, data=post_data))
        return self.http.get_value(result, 'loginuid'), self.http.get_value(result, 'logintoken')

    def checkstore(self):
        '''
        已认证琴行
        :return: 用户id和token
        '''
        post_data = {
            "cmd": "login",
            "params":
                {
                    "login_type": "a7d3bbc5-dcb7-53ff-2df1-af203a832b52",
                    "account": "正悦琴行",
                    "password": "123456",
                    "openid": ""
                }
        }
        post_data = json.dumps(post_data)
        result = json.loads(self.http.post(self.url_4 + self.login_path, data=post_data))
        return self.http.get_value(result, 'loginuid'), self.http.get_value(result, 'logintoken')

    def vipstore(self):
        '''
        vip琴行
        :return: 用户id和token
        '''
        post_data = {
            "cmd": "login",
            "params":
                {
                    "login_type": "a7d3bbc5-dcb7-53ff-2df1-af203a832b52",
                    "account": "伽音琴行",
                    "password": "123456",
                    "openid": ""
                }
        }
        post_data = json.dumps(post_data)
        result = json.loads(self.http.post(self.url_4 + self.login_path, data=post_data))
        return self.http.get_value(result, 'loginuid'), self.http.get_value(result, 'logintoken')
