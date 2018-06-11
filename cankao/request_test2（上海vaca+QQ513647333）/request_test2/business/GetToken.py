#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'vaca'
__description__:'从登录接口获取token'
__mtime__:2017/6/12
'''

import json
import requests
import hashlib
from readConfig import ReadConfig
from log import Log

ReadConfig = ReadConfig()
log = Log()
token = None


class GetToken:
    def __init__(self):
        # 从config。ini中提取数据
        self.data_address = ReadConfig.get_config("DATABASE", "data_address")
        self.login_path = ReadConfig.get_config("DATABASE", "login_path")
        self.hostname = ReadConfig.get_config("DATABASE", "hostname")
        self.code = ReadConfig.get_config("DATABASE", "code")
        username = ReadConfig.get_config("DATABASE", "username")
        password = ReadConfig.get_config("DATABASE", "password")
        # password参数必须是byte类型 ,hase_password以16进制的形式返回
        hase_password = hashlib.md5(password.encode('utf-8')).hexdigest()
        log.debug('加密后的密码是：%s' % hase_password)
        self.data = {"loginName": username, "password": hase_password}

    def get_token(self, data=None):
        '''获取登录的token'''
        global token
        r = requests.post(self.hostname + self.login_path, data=self.data)
        vjson_data = json.loads(r.text)  # 获取并处理返回的json数据
        if self.code == vjson_data['resCode']:
            vtoken = vjson_data['token']  # 获取token
            log.info("获取的token是：%s" % vtoken)
            return vtoken
        else:
            log.error("error：%s" % vjson_data['resDesc'])
            exit()


def main():
    tokendata = GetToken()
    tokendata.get_token()
if __name__ == '__main__':
    main()