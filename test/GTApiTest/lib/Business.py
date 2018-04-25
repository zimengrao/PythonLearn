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
        self.homepage = self.config.get('homepage')
        self.config = self.config.get('test')
        self.base_url = self.config.get('base_url')
        self.data_null, self.data_password_null, self.data_username_null, self.data_password_false, self.data_true = \
            self.config.get('login')
        self.guang_url = self.config.get('guangchang').get('guang_url')
        self.value = self.config.get('guangchang').get('value')

        # self.loginuid = self.config.get('loginuid')

    def login(self, data=None):
        """ 传入登录参数，返回json接口"""
        resp = json.loads(self.post(self.base_url, data=data))
        print(json.dumps(resp, indent=4, ensure_ascii=False))
        return resp

    def login_value(self):
        """ 调用登录接口，返回token和loginuid值"""
        resp = json.loads(self.post(self.base_url, data=self.data_true))
        # print(json.dumps(resp, indent=4, ensure_ascii=False))
        # print(resp)
        global token
        global loginuid
        token = self.get_value(resp, 'token')
        loginuid = self.get_value(resp, 'userid')
        # print(loginuid)

    def guangchang_url(self, guang_value):
        """ guang_value get('value')的取值"""
        resp = self.base_url + \
               self.guang_url.format(1, loginuid, token) + guang_value
        print(resp)
        resp = json.loads(self.get(resp))
        return resp

        # if self.assertEqual()
        # print(json.dumps(resp, indent=4, ensure_ascii=False))


