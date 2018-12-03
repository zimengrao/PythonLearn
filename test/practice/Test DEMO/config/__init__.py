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
                '//input[@id="user_login"]',    # input username
                '//input[@id="user_password"]',     # input passwords
                '//input[@value="登录"]',
            ],
            'assert_xpath':[
                '/html/body/div[1]/nav/div/ul[1]/li/ul/li[1]/a/text()'
            ]
        },
        'baidu':{
            'url': 'https://www.baidu.com/',
            'keywords': '淘宝',
            'xpath': [
                '//*[@id="kw"]',    # search input element
                '//*[@value="百度一下"]',   # click button element
                '//*[@id="s_tab"]/a[2]',    # click tieba element
            ],
            'assert_xpath':[
                '//title/text()',
                '//*[@class=" card_title_fname"]/text()'

            ]
        }
    }