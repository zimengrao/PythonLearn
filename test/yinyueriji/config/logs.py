"""
@Name: logs
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/10/29
"""

import logging
from config.cnf import Config
import datetime
import os


class Log:
    def __init__(self):
        logging.config.fileConfig('E:/myAppiumproj/request_test2/util/log.ini')
        # create logger
        self.logger = logging.getLogger('request')

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)


def main():
    logyyx = Log()
    logyyx.debug('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.war('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.cri('一个致命critical信息')
# class LogConfig:
#     @staticmethod
#     def init(path):
#         global logger
#
#         if not os.path.exists('./log'):
#             os.mkdir('./log')
#
#         nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         logging.basicConfig(level=logging.INFO,
#                             format='%(asctime)s %(levelname)s %(message)s',
#                             datefmt='%Y-%m-%d %H:%M:%S',
#                             filename = './log/'+nowTime+'.log',
#                             filemode='a')
#         logger = logging.getLogger()
#
#
#     @staticmethod
#     def getLogger():
#         return logger
