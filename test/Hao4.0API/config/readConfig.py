"""
@Name: readConfig
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/9
"""

import os
import configparser

pro_dir = os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.join(pro_dir, 'config.ini')

class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)

    def get_config(self, field, key):
        result = self.cf.get(field, key)
        return  result

    def set_config(self, field, key, value):
        fd = open(config_path, 'w')
        self.cf.set(field, key, value)
        self.cf.write(fd)