"""
@Name: business
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/9
"""


from lib.client import HttpHandler
from config.cnf import Config
from config.data import ExcelData
import json
import ddt

token = None
loginuid = None

data_user = ExcelData().readData('user')


@ddt.ddt
class BusinessApi(HttpHandler):
    def __init__(self):
        super(BusinessApi, self).__init__()
        self.http = HttpHandler()
        self.config = Config()
        self.excel = ExcelData()

        self.url = self.config.get_config('HTTP', 'baseurl')
        self.url_dev = self.config.get_config('HTTP', 'baseurl_dev')
        self.username = self.config.get_config('DATABASE', 'username')
        self.password = self.config.get_config('DATABASE', 'password')
        self.login_path = self.config.get_config('DATABASE', 'login_path')
        self.code = self.config.get_config('DATABASE', 'code')

        self.data_address = self.config.get_config('DATABASE', 'data_address')
        self.port = self.config.get_config('HTTP', 'port')

        self.data = {
            'api': self.login_path,
            'username': self.username,
            'password': self.password
        }

    def get_token(self):
        ''' 获取登录的token '''
        global token
        global loginuid
        # print(self.url,self.data)

        resp = json.loads(self.http.post(self.url, data = self.data))
        # print(resp)
        token = str(self.http.get_value(resp, 'token'))
        loginuid = str(self.http.get_value(resp, 'userid'))
        return token, loginuid

    def set_token(self):

        self.get_token()
        self.config.set_config('DATABASE', 'token', token)
        self.config.set_config('DATABASE', 'loginuid', loginuid)
        return token, loginuid

    def get_all_user(self):
        # print(len(data_user))
        # print(data_user[0])
        for data in data_user:
            data = data.get('body')
            data = json.loads(data)
            resp = json.loads(self.http.post(self.url, data = data))
            if self.http.get_value(resp, 'err_msg') == 'success':
                self.excel.writeData()
            print(resp)
        # print(resp)

if __name__ == '__main__':
    lib = BusinessApi()
    lib.get_all_user()