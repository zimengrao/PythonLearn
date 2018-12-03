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
from config.mysql import MysqlData

import json
import random
import ast
import collections

# get_user = ExcelData('user').readData()

class BusinessApi(HttpHandler):
    def __init__(self):
        super(BusinessApi, self).__init__()
        self.http = HttpHandler()
        self.config = Config()
        self.read = ExcelData
        self.mysql = MysqlData()


        self.url = self.config.get_config('HTTP', 'baseurl') # 4.0PC网站地址
        self.api = self.config.get_config('HTTP', 'webapi') # 4.0-appapi接口地址
        self.username = self.config.get_config('DATABASE', 'username')
        self.password = self.config.get_config('DATABASE', 'password')
        self.login_path = self.config.get_config('DATABASE', 'login_path') # 登录接口API

        self.data_address = self.config.get_config('DATABASE', 'data_address')
        self.port = self.config.get_config('HTTP', 'port')

        self.post_data= {
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
        resp = json.loads(self.http.post(self.api + self.login_path, data = post_data))
        # print(resp)
        if self.get_value(resp, 'info') == '登录成功！':
            token_data = str(self.http.get_value(resp, 'logintoken'))
            loginuid_data = str(self.http.get_value(resp, 'loginuid'))
            self.config.set_config('DATABASE', 'token', token_data)
            self.config.set_config('DATABASE', 'loginuid', loginuid_data)
            return loginuid_data,token_data
        else:
            print('登录失败或接口错误')

    def login(self, userid, password):
        '''

        :return: 用户登录
        '''
        data = {"cmd": "login",
                "params":
                    {
                        "login_type": "a7d3bbc5-dcb7-53ff-2df1-af203a832b52",
                        "account": "Yilia",
                        "password": "hqs123",
                        "openid": ""
                    }
                }
        select_data = "SELECT tc002_name, tc002_login_token from gt002_user_auth where tc001_user_id = %s" %userid
        select_data = self.change_list(select_data)
        data['params']['account'] = select_data[0]
        data['params']['password'] = password
        data = json.dumps(data)
        result = json.loads(self.http.post(self.api + self.login_path, data=data))
        return self.http.get_value(result, 'logintoken')

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
        l = 4
        k = 1
        for data in self.data_user:
            data = data.get('body')
            # print(data)
            data = ast.literal_eval(data)
            resp = json.loads(self.http.post(self.url, data = data))
            # print(resp )
            if self.http.get_value(resp, 'err_msg') == 'success':
                self.write0.write(k,j, self.http.get_value(resp, 'userid'))
                # print(k,j,self.http.get_value(resp, 'userid'))
                self.write0.write(k,i, self.http.get_value(resp, 'token'))
                # print(k,i,self.http.get_value(resp, 'token'))

            self.write0.write(k,l, self.http.get_value(resp, 'err_msg'))
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

    def repeat_test(self, items):
        '''
        判断列表中是否有重复的数据
        :param items: 列表
        :return:
        '''
        if len(items) > 0:
            for item in items:
                if items.count(item) != 1:
                    print('detail_id重复的数据有{}'.format(item))
                    return False
                else:
                    print('detail_id没有重复的数据')
                    return True
        else:
            return "列表没有数据"

    def data_contrast(self, sql, result, data=None):
        '''
        对比数据库的数据和接口请求数据是否相同
        :param sql: 查询数据库语句
        :param result: 调用接口数据
        :param data: 对比数据对象
        :return:
        '''

        i = 0
        select_data = self.mysql.selectAll(sql)
        # print(select_data)
        if type(result) == list:
            for item in result:
                if item == select_data[0][i]:
                    return True
                else:
                    print('接口获取数据{}，和查询数据{} 不相等'.format(item, select_data)[0][i])
                    return False
        else:
            print(select_data)
            for item in self.http.get_value(result, 'data'):
                print(item, select_data[0][i])
                if item.get(data) == select_data[0][i]:
                    return True
                else:
                    print('接口获取数据{}，和查询数据{} 不相等'.format(item, select_data)[0][i])
                    return False
                i += 1

    def change_list(self, sql):
        '''

        :param sql: sql语句
        :return: 将tuple转为list
        '''
        select_data = self.mysql.selectAll(sql)
        list_datas = []
        if len(select_data) == 1:
            for item in select_data[0]:
                list_datas.append(item)
            return list_datas
        else:
            for item in select_data:
                list_datas.append(item[0])
            return list_datas

    def api_status_check(self, resp):
        '''

        :param resp: 接口请求返回数据
        :return:
        '''
        err_msg = self.http.get_value(resp, 'err_msg')
        if resp !=200:
            if err_msg == 'success':
                return True
            elif err_msg == 'error' and self.http.get(resp, 'info') == '没有更多信息':
                return True
            elif err_msg == 'error' and self.http.get(resp, 'info') == '没有更多信息':
                return True
            else:
                print(resp)
                return False

# if __name__ == '__main__':
#     bus=BusinessApi()
#     bus.login(2940,'hqs123')
    # bus.change_list("SELECT tc002_name,tc002_login_token from gt002_user_auth where tc001_user_id = 2940")
