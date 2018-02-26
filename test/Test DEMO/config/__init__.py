"""
@Name: __init__
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/2/1
"""

class Config:
    enum = {
        'login':{
            'url': 'https://testerhome.com/account/sign_in',
            'username': 'zimengrao',
            'password': '1qazXSW@',
            'xpath': [
                '//input[@id="user_login"]',
                '//input[@id="user_password"]',
                '//input[@value="登录"]',
            ],
            'assert_xpath':[
                '/html/body/div[1]/nav/div/ul[1]/li/ul/li[1]/a/text()'
            ]
        }
    }