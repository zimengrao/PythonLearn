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
url = 'http://v.juhe.cn/weather/index?format=2&cityname={}&key={}'
city_name = '北京'
key = '8914a2e03dc4cbed5178b9b5464496fc'