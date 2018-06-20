"""
@Name: business
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/9
"""


from lib.client import HttpHandler
from config.cnf import Config
from config.ReadExcel import ExcelData
from config.WriteExcel import WriteData

import json
import random
import ast
import collections

token = None
loginuid = None

# get_user = ExcelData('user').readData()

class BusinessApi(HttpHandler):
    def __init__(self):
        super(BusinessApi, self).__init__()
        self.http = HttpHandler()
        self.config = Config()
        self.read = ExcelData

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

    def write_user(self, num):
        '''

        :param num: 写入第几个工作簿
        :return:
        '''
        # print(len(data_user))
        # print(data_user[0])
        self.data_user = ExcelData('user').readData()
        self.write0 = WriteData(num)
        i = 2
        j = 3
        k = 1
        for data in self.data_user:
            data = data.get('body')
            data = ast.literal_eval(data)
            resp = json.loads(self.http.post(self.url, data = data))
            # print(resp )
            if self.http.get_value(resp, 'err_msg') == 'success':
                self.write0.write(k,j, self.http.get_value(resp, 'userid'))
                # print(k,j,self.http.get_value(resp, 'userid'))
                self.write0.write(k,i, self.http.get_value(resp, 'token'))
                # print(k,i,self.http.get_value(resp, 'token'))
            k += 1

        bookname = random.randint(0,100)
        self.write0.save('{}.xls'.format(bookname))

    def write_body(self, params, num):
        '''
        将body写入excel中
        :param params: 需要传入参数，比如礼物列表活动类型
        :param num: 写入工作簿的第几个表格
        :return:
        '''
        self.get_user = self.read('user').readData()
        write2 = WriteData(num)
        dict_body = collections.OrderedDict()
        k = 1
        i = 2
        for data in self.get_user:
            self.loginuid = data.get('loginuid')
            self.logintoken = data.get('token')
            if self.loginuid != '':
                self.loginuid = int(self.loginuid)
                dict_body['loginuid'] = self.loginuid
                dict_body['logintoken'] = self.logintoken
                dict_body['params'] = params
                body = json.dumps(dict_body)
                # body = str(dict_body)
                write2.write(k,i, body)
                # print(body)

                k += 1
        bookname = random.randint(0, 100)
        write2.save('{}.xls'.format(bookname))
        # return dict_body
#
# if __name__ == '__main__':
#     lib = BusinessApi()
#     lib.write_user(0)
#     dd = {"activity_id": "2f0fc929-58cd-bbc5-403a-0c6d7d18c376"}
#     lib.write_body(dd, 2)
#     # bookname = random.randint(97, 122)
#     # print(bookname)
