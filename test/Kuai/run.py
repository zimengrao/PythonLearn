"""
@Name: run
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/22
"""

from lib.client import HttpHandler
import json

class KuaiShou:
    def __init__(self):
        super(KuaiShou, self).__init__()
        self.http = HttpHandler()


        self.url = 'http://api.ksapisrv.com/rest/n/feed/myfollow?appver=5.7.5.508&did_gt=1529667194844&did=31550242-1FC2-44CE-8C6B-9567A204F75E&c=a&ver=5.7&ud=997239509&lon=121.3978173993196&lat=31.17402504630572&sys=ios11.3.1&mod=iPhone7%2C2&net=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8_5'

        self.headers = {
            'Host': 'api.ksapisrv.com',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'X-REQUESTID': '28541722',
            'Accept': 'application/json',
            'User-Agent': 'kwai-ios',
            'Accept-Language': 'zh-Hans-CN;q=1, zh-Hant-CN;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Length': '300'
        }

        self.data = '__NStokensig=f8e38000e5bebe14816985208ce4fb2d945b03a81a9755b26be40d63af8aaa1d&client_key=56c3713c&count=20&country_code=cn&id=65&language=zh-Hans-CN%3Bq%3D1%2C%20zh-Hant-CN%3Bq%3D0.9&refreshTimes=11&sig=e45925a0c214587ce3dcf5468aa62cba&source=1&token=f7c4c199c3044ce1a0431f6a40818bf3-997239509&type=6'
        self.data = self.data.encode('utf-8')

        # single = '__NStokensig=655a439189df16f3c8dd12346b20fd2b2abf787ea70438dd9cb7b6ad421c1f95&client_key=56c3713c&content=%E8%BF%98%E8%A6%81%E4%BA%BA%E5%90%97&country_code=cn&language=zh-Hans-CN%3Bq%3D1%2C%20zh-Hant-CN%3Bq%3D0.9&photo_id=5216294275275128978&refer=ks%3A%2F%2Fphoto%2F46069179%2F5216294275275128978%2F3%2F1_i%2F1605145365382963207_h123%23addcomment&sig=7d215b7e379b2ca08adea7edf47e0899&token=f7c4c199c3044ce1a0431f6a40818bf3-997239509&user_id=46069179'
        # self.single = single.encode('utf-8')
    def review(self):
        resp = self.http.post(url=self.url, data=self.data, headers=self.headers)
        # print(resp)
        resp = json.loads(resp)
        resp = self.http.get_value(resp, 'feeds')
        for item in resp:
            print(item.get('photo_id'))
        # print(resp)

if __name__ == '__main__':
    kk = KuaiShou()
    kk.review()
