
"""
@Name: client.py
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/9
"""

from requests import Session
from user_agent import generate_user_agent

from lib.web.recursion import GetDictParam


class HttpHandler(GetDictParam):
    def __init__(self):
        super(HttpHandler, self).__init__()
        self.session = Session()
        self.headers = {
            'User-Agent': generate_user_agent()
        }
        # self.session.cert = ""

    def get(self, url):
        """ 用seesion对象发出一个get请求，返回text格式的数据"""
        resp = self.session.get(url, headers=self.headers).text
        return resp

    def post(self, url, data=None, json=None):
        """ 用seesion对象发出一个post请求，返回text格式的数据"""
        if json:
            return self.session.post(url, json=json).status_code
        return self.session.post(url, data=data).text

    def post_code(self, url, data=None, json=None):
        '''

        :param url:
        :param data:
        :param json:
        :return: post请求状态码
        '''
        return self.session.post(url, json=json).status_code