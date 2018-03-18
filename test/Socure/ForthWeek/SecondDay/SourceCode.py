"""
@Name: SourceCode
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/3/13
"""

import requests
import json
from lxml import etree



# url = 'http://v.juhe.cn/weather/index?format=2&cityname={}&key={}'
# city_name = '北京'
# key = '8914a2e03dc4cbed5178b9b5464496fc'
#
# url = url.format(city_name, key)
#
# response.json()返回的是一个字典类型的数据结构
# result = requests.get(url).json()

# print(result)
# print(result.get('result').keys())
# for item in (result.get('result').get('future')):
#     print(item)
# print(result.get('result').get('today'))

# # 如何去断言一个接口是否成功
# assert result.get('reason') == 'successed!'
# assert result.get('error_code') == 0
# # json.dumps 是将一个字典类型的数据转换成string类型
# string_result = json.dumps(result, indent=4, ensure_ascii=False)
# print(string_result)
