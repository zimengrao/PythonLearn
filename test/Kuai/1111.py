"""
@Name: 1111
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/7/4
"""

import requests
import json

url = 'http://api.ksapisrv.com/rest/n/feed/myfollow?appver=5.7.5.508&did_gt=1529667194844&did=31550242-1FC2-44CE-8C6B-9567A204F75E&c=a&ver=5.7&ud=997239509&lon=121.3978173993196&lat=31.17402504630572&sys=ios11.3.1&mod=iPhone7%2C2&net=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8_5'

headers = {
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

data = '__NStokensig=f8e38000e5bebe14816985208ce4fb2d945b03a81a9755b26be40d63af8aaa1d&client_key=56c3713c&count=20&country_code=cn&id=65&language=zh-Hans-CN%3Bq%3D1%2C%20zh-Hant-CN%3Bq%3D0.9&refreshTimes=11&sig=e45925a0c214587ce3dcf5468aa62cba&source=1&token=f7c4c199c3044ce1a0431f6a40818bf3-997239509&type=6'
data = data.encode('utf-8')

resp = requests.post(url = url, data = data, headers = headers).text
resp = json.loads(resp)
print(resp)