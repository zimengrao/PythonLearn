"""
@Name: __init__.py
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/8
"""

class Config:

    enum = {
        'baidu':{
            'home_page':{
                'start_url': 'https://www.baidu.com/',
                'xpath':  [
                    '//*[@id="kw"]',    # search input element
                    '//*[@value="百度一下"]',   # click button element
                    # '//*[@id="s_tab"]/a[2]',    # click tieba element
                    '//*[@id="4"]/h3/a',
                ],
                'keyword': '今日头条',
                'assert_info': [
                    '//title/text()'
                ]
            },
            'baike': {
                'start_url': 'https://baike.baidu.com/item/%E4%BB%8A%E6%97%A5%E5%A4%B4%E6%9D%A1/4169373?fr=aladdin',
                'assert_xpath': [
                    '/html/body/div[4]/div[2]/div/div[2]/div[7]/dl[1]/dd[1]/text()',
                ]
            }
        },
        'iqiyi':{
            'home_page': 'http://www.iqiyi.com/',
            'xpath': [
                '//*[@id="block-C"]/div/div/div/div/div/ul[2]/li[1]/a',
            ],
            'assert_xpath': [
                '//title/text()',
            ]
        }
    }
