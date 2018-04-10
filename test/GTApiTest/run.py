"""
@Name: run
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/4/9
"""

import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_siute = unittest.defaultTestLoader.discover('tests', pattern='test*.py')
    result = BeautifulReport(test_siute)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')