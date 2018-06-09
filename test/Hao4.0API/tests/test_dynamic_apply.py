"""
@Name: test_dynamic_apply
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/9
"""

import unittest

import ddt

from lib.business import BusinessApi
from lib.client import HttpHandler


class DynamicApply(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.http = HttpHandler()
        cls.lib = BusinessApi()
        cls.excel = cls.lib.excel

    @ddt.data(*.next())
    def test_dynamic_Apply(self):

