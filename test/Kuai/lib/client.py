"""
@Name: client
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/22
"""

from requests import Session
from user_agent import generate_user_agent
from lib.recursion import GetDictParam

class HttpHandler(GetDictParam):
    def __init__(self):
        super(HttpHandler, self).__init__()
        self.session = Session()
        self.headers = {
            'User_Agent': generate_user_agent()
        }

    def get(self, url):
        resp = self.session.get(url).text
        return resp

    def post(self, url, data=None, json=None, headers=None):
        if json:
            return self.session.post(url, json=json, headers=headers).text
        return self.session.post(url, data=data, headers=headers).text
