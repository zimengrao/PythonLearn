"""
@Name: run
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/4/8
"""
import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('tests', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')


# import requests
# url = 'http://test.greattone.net/e/appapi/'
# data = {
#     'api': 'user/login',
#     'username': '贾老师',
#     'password': '123456',
# }
# header = {
#     # 'User-Agent': 'okhttp/3.3.1',
#     # 'Accept-Encoding': 'gzip',
#     # 'Content-Type': 'application/x-www-form-urlencoded',
#     # 'cookie': 'platform=android; model=Coolpad; device_id=00000000-d8967aa8; version=Vx.0.0'
# }
# response = requests.post(url, data=data, headers=header)
# print(response.text)
