"""
@Name: unca
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/2/25
"""

import unittest

class TestDemo(unittest.TestCase):
    def SetUp(self):
        print('测试方法开始执行')

if __name__ == '__main__':
    unittest.main()