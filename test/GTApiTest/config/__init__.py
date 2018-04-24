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
            'guangchang': {
                'guang_url': '?api=info/guanlist&classid=1&extra=shipin,hai_id,hai_video,hai_photo,hai_petition,hai_name&pageIndex=1&pageSize=20&loginuid={}&logintoken={}',
                'value': [
                    '&timehot=', # 音乐广场参数，全站动态和音乐广场一样
                    '&query=onclick', #  推荐动态参数
                    '&timehot=4&ismember=1&query=onclick', # 年热动态参数
                    '&timehot=5&ismember=1&query=onclick', # 季热动态参数
                    '&timehot=3&ismember=1&query=onclick', # 季热动态参数
                    '&timehot=2&ismember=1&query=onclick', # 周热动态参数
                ],

            }
        }
    }
