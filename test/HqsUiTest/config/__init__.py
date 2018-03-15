"""
@Name: __init__.py
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/9
"""

class Config:
    enum = {
        'login':{
            'url': 'http://test.greattone.net:8080/',
            'username': '贾老师',
            'password': '123456',
            'xpath': [
                '//*[@id="loginBtn"]/a',    # 登录element
                '//input[@id="username1"]',
                '//input[@id="password"]',
                '//input[@id="submit"]',
            ],
            'assert_xpath': [
                '/html/body/div[10]/div[2]/div/div[1]/div/div[2]/span[1]/text()',   # 用户名element
            ]
        }
    }