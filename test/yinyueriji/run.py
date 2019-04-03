"""
@Name: run.py
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/11
"""

import unittest
from BeautifulReport1 import BeautifulReport

def app_api():
    test_suite = unittest.defaultTestLoader.discover('tests/test_api_app/api', pattern='test1*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='appapi测试报告', description='appapi测试报告', log_path='report')

def web_api():
    test_suite = unittest.defaultTestLoader.discover('tests/test_api_web/api', pattern='test2.py')
    result = BeautifulReport(test_suite)
    result.report(filename='appapi测试报告', description='appapi测试报告', log_path='report')

def andriod_ui():
    test_suite = unittest.defaultTestLoader.discover('tests/test_ui_andriod', pattern='test2*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='andriod功能测试报告', description='appapi测试报告', log_path='report')

def web_ui():
    test_suite = unittest.defaultTestLoader.discover('tests/test_ui_web', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='appapi测试报告', description='appapi测试报告', log_path='report')

if __name__ == '__main__':
    # app_api()
    andriod_ui()


