"""
@Name: request
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2019/6/24
"""

import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class RunMain:

    def __init__(self,url,method,data=None):
        self.res = self.run_main(url,method,data)

    def post(self, url, data):
        self.res = requests.post(url=url,data=data,verify=False).text
        return self.res

    def get(self, url, data):
        self.res = requests.get(url=url, data=data,verify=False).text
        return self.res

    def run_main(self, url, method, data=None):
        self.res = None
        if method == 'GET':
            self.res = self.post(url,data)
        else:
            self.res = self.get(url, data)
        return self.res

# if __name__ == '__main__':
#
#     run = RunMain().run_main

