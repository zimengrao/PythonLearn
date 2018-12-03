"""
@Name: test_login
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/11/30
"""

import lib
import time
import unittest
from pc.business import Business

class HqsTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lib =Business

    def setUp(self):
        self.driver = self.lib.driver()

    def tearDown(self):
        self.driver.quit()

    def test_yinyueriji_is_ok(self):
        ''' 音乐日记网站 is ok'''
        pass