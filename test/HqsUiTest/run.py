
"""
@Name: run
@Version:
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/9
"""

import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('tests', pattern='test_dynamic_join.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试default报告', log_path='report')