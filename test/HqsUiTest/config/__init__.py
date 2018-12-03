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

                'title': '标题',
                'content': '内容详细信息',

                'click_dynamic': [
                    '/html/body/div[10]/div[3]/div[1]/div[1]/ul/li[1]',
                    '//div[@class="singleMiddle"]/div/div/ul/li[2]',
                    '/html/body/div[10]/div[3]/div[1]/div[1]/ul/li[3]'
                ],

                'video': {
                    'video':[
                        '//input[@name="title"]', # 视频标题 element
                        '//*[@id="videoDes"]',  # 视频内容 element
                        '//*[@class="singleMiddle"]/div[1]/div[2]/form/div[2]/div[1]/input[@id="fileVideo"]',  # 视频上传地址 element
                        '//*[@class="singleMiddle"]/div[1]/div[2]/form/div[6]/input',  # 发布视频 element
                    ],

                    'video_file': 'E:\\桌面\\视频\\20180601.mp4', # 本地视频地址路径

                },

                'music': {
                    'music': [
                        '//*[@class="singleMiddle"]/div[1]/div[3]/form/div[1]/input[@type="text"]', # 音乐标题element
                        '//div[@class="singleMiddle"]/div[1]/div[3]/form/div[4]/textarea', # 音乐内容 element
                        '//*[@id="selectfilesMusic"]',  # 选择音乐文件 element
                        '//*[@id="postfilesMusic"]', # 上传音乐 element
                        '/html/body/div[10]/div[3]/div[1]/div[3]/form/div[5]/input',  # 发布音乐 element
                    ],

                    'music_file': 'F:\\CloudMusic\\自由.mp3' # 本地音乐地址路径

                },

                'photo': {
                    'photo': [
                        '//*[@class="singleMiddle"]/div[1]/div[4]/form/div[1]/input[@type="text"]',  # 图片标题element
                        '//*[@class="singleMiddle"]/div[1]/div[4]/form/div[3]/textarea[@name="smalltext"]',  # 图片内容 element
                        '//*[@class="singleMiddle"]/div[1]/div[4]/form/div[2]/a',  # 选择文件 element
                        '//*[@class="singleMiddle"]/div[1]/div[4]/form/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div/div[2]',  # 选择图片 element
                        '//*[@class="singleMiddle"]/div[1]/div[4]/form/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]', # 继续上传图片 element
                        '//*[@id="uploader"]/div[2]/div[3]/div[2]',  # 开始上传 element
                        '//*[@class="singleMiddle"]/div[1]/div[4]/form/div[4]/input',  # 发布图片动态 element
                    ],

                    'photo_file': [
                        'E:\\桌面\\图片\\1.jpg',
                        'E:\\桌面\\图片\\2.jpg',
                        'E:\\桌面\\图片\\3.jpg',
                        'E:\\桌面\\图片\\4.jpg',
                        'E:\\桌面\\图片\\5.jpg'
                    ]
                }
            },

            'assert_xpath': [
                '/html/body/link[5]/@href',  # 打开好琴声网站验证
                '/html/body/div[1]/div/div[4]/div/ul/li[4]/a/text()',  # 登录成功确认
                '/html/body/div[7]/div[2]/div[1]/div/ul/li[1]/div[1]/div[2]/a/h3/text()', # 发帖成功
            ],
        },
        'aliyun':{
            'aliyun': {
                'url': 'https://www.aliyun.com/',
                'xpath': '//*[@id="common-topbar-login-btn"]/a'
            },
            'login': {
                'username': 'sandner@franzsandner.com',
                'password': 'Haoqinsheng2016++',
                'iframe_id': 'alibaba-login-box',
                'xpath': [
                    '//*[@id="fm-login-id"]',
                    '//*[@id="fm-login-password"]',
                    '//*[@id="nc_1_n1z"]',
                    '//*[@id="fm-login-submit"]'
                ],
                'assert_info': [
                    '/html/body/div[2]/div/div/div[3]/div[2]/div[1]/div/div[2]/div[2]/p[2]/text()'
                ]
            },
            'xpath_js': [
                '//*[@class="common-topbar-menu"]/div[2]/a',
                '/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/ul/li[4]/a/div/span',
                '//*[@id="app"]/div/div/div[1]/div[2]/div/div[3]/a[6]/span',
                '//*[@id="app-content"]/main/div/div[2]/div[1]/div[2]/a',
                '//*[@id="app-content"]/main/div/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[3]/td[3]/div',
                '//*[@id="app-content"]/main/div/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[5]/td[3]/div/a'
            ]
        }
    }