"""
@Name: __init__.py
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/9
"""

class Config:
    enum = {
        'hqs':{

            'url': 'http://test.greattone.net/',

            'login': {
                'username': '贾老师',
                'password': '123456',
                'xpath_login': [
                    '//*[@id="loginBtn"]/a',  # 页面登录element
                    '//input[@id="username1"]',
                    '//input[@id="password"]',
                    # '//*[@id="submit"]',
                    '/html/body/div[2]/form/ul/li[4]',  # 对话框登录element
                ],
            },

            'dynamic':{
                'xpath_dynamic': [
                    '/html/body/div[1]/div/div[2]/ul/li[2]/a',  # 音乐广场element
                    '/html/body/div[7]/div[1]/div[2]/a',  # 我要发帖element
                ],

                'send': '//*[@id="subVideo"]',
                'value': '测试发帖',

                'video': {
                    'xpath_video': [
                        '//*[@id="videoTitle"]',  # 个人中心视频发帖element
                        '//*[@id="fileVideo"]',  # 上传视频element
                    ],

                    'path_photo': 'E:\\桌面\\视频\\20180601.mp4'
                },

                'photo': {
                    'xpath_photo': [
                        '//*[@id="videoTitle"]',  # 个人中心视频发帖element
                        '//*[@id="fileVideo"]',  # 上传视频element
                    ],

                    'path_photo': 'E:\\桌面\\视频\\20180601.mp4'

                },

                'music': {
                    'xpath_video': [
                        '//*[@id="videoTitle"]',  # 个人中心视频发帖element
                        '//*[@id="fileVideo"]',  # 上传视频element
                    ],

                    'video_path': 'E:\\桌面\\视频\\20180601.mp4'

                }

            },

            'assert_xpath': [
                '/html/body/link[5]/@href',  # 打开好琴声网站验证
                '/html/body/div[1]/div/div[4]/div/ul/li[4]/a/text()',  # 登录成功确认
            ],
        }
    }