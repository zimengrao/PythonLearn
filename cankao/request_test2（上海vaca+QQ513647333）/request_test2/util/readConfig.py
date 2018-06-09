#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'vaca'
__description__:'读取配置文件信息'
__mtime__:2017/6/10
'''
import os
import configparser
from log import Log

log = Log()


proDir = os.path.split(os.path.realpath(__file__))[0]   # 获取当前py文件地址
configPath = os.path.join(proDir, "config.ini")         # 组合config文件地址


class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_config(self, field, key):
        '''获取config.ini信息'''
        result = self.cf.get(field, key)
        # log.debug('%s的%s是：%s' % (field, key, result))
        return result

    def set_config(self, field, key, value):
        '''修改config.ini信息'''
        fd = open(configPath, "w")
        self.cf.set(field, key, value)
        log.debug('%s的%s修改成功 ,value=%s' % (field, key, value))
        self.cf.write(fd)


def main():
    config = ReadConfig()
    config.get_config("DATABASE", "token")
    config.set_config("DATABASE", "token", "454154234")
if __name__ == '__main__':
    main()