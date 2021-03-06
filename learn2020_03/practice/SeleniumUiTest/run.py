"""
@Name: run
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/8
"""

import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('tests', pattern='test_baidu.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')
