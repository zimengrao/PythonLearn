"""
@Name: ceshi
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/9
"""

import unittest

import ddt
from htest.excelutil import ExcelUtil

m='exceldata.xlsx'
excel = ExcelUtil('F:\\python\\PythonLearn\\test\\Hao4.0API\\data\\testdata.xlsx', 'Sheet1')


@ddt.ddt
class DataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start')

    @classmethod
    def tearDownClass(cls):
        print('stop')

    @ddt.data(*excel.next())
    def testLogin(self, data):
        print(data['username'])
        print(data['password'])
        print(data['country'])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(DataTest)
    unittest.TextTestRunner(verbosity=2).run(suite)