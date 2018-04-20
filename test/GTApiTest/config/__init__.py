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
            'login': [
                {
                    'api': 'user/login'  # 用户名密码为空
                },
                {
                    'api': 'user/login',  # 密码为空
                    'username': '读后感客户端上老师'
                },
                {
                    'api': 'user/login',  # 用户名为空
                    'password': '565699'
                },
                {
                    'api': 'user/login',  # 正确的用户名，错误的密码
                    'username': '贾老师',
                    'password': '565699'
                },
                {
                    'api': 'user/login',  # 错误的用户名，错误的密码
                    'username': '贾老师',
                    'password': '123456'
                }

            ],
            'guangchang': '?api=info/guanlist&classid=1&extra=shipin,hai_id,hai_video,hai_photo,hai_petition,hai_name&pageIndex=1&pageSize={}&loginuid={}&logintoken={}&timehot='
        }
    }
