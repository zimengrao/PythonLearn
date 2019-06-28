"""
@Name: test_method
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2019/6/24
"""

import unittest
from base import demo
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Music(unittest.TestCase):

    # def setUp(self):
    #     self.run = demo.RunMain()
    #     print('测试开始')

    @classmethod
    def setUpClass(cls):
        cls.run = demo
        print('测试开始')

    @classmethod
    def tearDownClass(cls):
        print('测试完成')

    def test1_is_ok(self):
        # url = 'https://t-webapi.yinyueriji.net/index.php/user-info/store'
        # data = '{"cmd":"check","params":{"province":"","city":"","country":"","keyword":"","desc":1,"page":1,"pageSize":10}}'
        # self.res = self.run.RunMain(url,'POST',data)
        # print(self.res)
        pass
if __name__ == '__main__':
    unittest.main()