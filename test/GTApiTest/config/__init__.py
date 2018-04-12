"""
@Name: __init__.py
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/4/10
"""

class Config:

    enum = {
        'GTApi': {
            'base_url': 'http://test.greattone.net/e/appapi/',
            'login': {
                'data': {
                    'api': 'user/login'  # 用户名密码为空
                },
                'data1': {
                    'api': 'user/login',  # 密码为空
                    'username': '读后感客户端上老师'
                },
                'data2': {
                    'api': 'user/login',  # 用户名为空
                    'password': '565699'
                },
                'data3': {
                    'api': 'user/login',  # 正确的用户名，错误的密码
                    'username': '贾老师',
                    'password': '565699'
                },
                'data4': {
                    'api': 'user/login',  # 错误的用户名，错误的密码
                    'username': '贾老师',
                    'password': '123456'
                },
            },
            'kdkdk': 'oo'
        },

    }

