"""
@Name: test_unittest_method
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/2/25
"""

# 如果tests文件夹中没有__init__.py文件的话，右键有在unittest运行本文件
import unittest
from tests.login.test_case_login import TesterHomeCases

class MethodTest(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(1,1)

    def test_not_null(self):
        self.assertIsNotNone('text')

    def test_unll(self):
        self.assertIsNone(None)

# main 告诉程序的入口文件
if __name__ == '__main__':
    unittest.main()