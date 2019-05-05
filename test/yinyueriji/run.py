"""
@Name: run.py
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/11
"""

import unittest
from BeautifulReport1 import BeautifulReport as be1
from BeautifulReport import BeautifulReport as be2
import threading

def app_api():
    test_suite = unittest.defaultTestLoader.discover('tests/test_api_app/api', pattern='test100*.py')
    result = be1(test_suite)
    result.report(filename='appapi测试报告', description='appapi测试报告', log_path='report')

def web_api():
    test_suite = unittest.defaultTestLoader.discover('tests/test_api_web/create', pattern='test2*.py')
    result = be1(test_suite)
    result.report(filename='webapi测试报告', description='webapi测试报告', log_path='report')

def andriod_ui():
    test_suite = unittest.defaultTestLoader.discover('tests/test_ui_andriod', pattern='test2_*.py')
    result = be2(test_suite)
    result.report(filename='andriod_ui测试报告', description='andriod_ui测试报告', log_path='report')

def web_ui():
    test_suite = unittest.defaultTestLoader.discover('tests/test_ui_web', pattern='test*.py')
    result = be1(test_suite)
    result.report(filename='web_ui测试报告', description='web_ui测试报告', log_path='report')

if __name__ == '__main__':
    # app_api()
    # andriod_ui()
    web_api()
    # threads = []
    # t1 = threading.Thread(target=andriod_ui())
    # threads.append(t1)
    # t2 = threading.Thread(target=app_api())
    # threads.append(t2)
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    # t.join()
    # print('ok')

