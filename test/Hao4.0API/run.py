"""
@Name: run.py
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/11
"""

import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('tests', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试default报告', log_path='report')

#
# import xlrd
#
# excel_path = 'E:\\桌面\\testdata.xls'
# data = xlrd.open_workbook(excel_path)
# table = data.sheets()[0]
# rows = table.nrows
# cols = table.ncols
# for i in range(rows):
#     list1 = table.row_values(i)
#     print(i)
#     print(list1)