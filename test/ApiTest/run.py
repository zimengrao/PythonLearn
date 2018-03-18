"""
@Name: run
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/16
"""

import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests', pattern='test_*.py')
    report = BeautifulReport(suite)
    report.report(filename='测试报告', description='测试deafult报告', log_path='report')