"""
@Name: test1_create_dynamic
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2019/1/22
"""
import json
import unittest

import ddt

from lib.web.business import BusinessApi
from lib.web.client import HttpHandler
from config.ReadExcel import ExcelData
from config.cnf import Config
from config.mysql import MysqlData

data= ExcelData('cappapi').readData()

@ddt.ddt
class HqsApi(unittest.TestCase):
    @classmethod
    def setUxxlass(cls):
        cls.http = HttpHandler()
        cls.lib = BusinessApi()
        cls.mysql = MysqlData()
        cls.config = Config()
        cls.user = cls.lib.get_token()

    # @ddt.data(*data[6:7])
    # def test1_create_dynamic_video_is_ok(self, data):
    #     ''' 发布视频帖 '''
    #
    #     self.case_name = data['API_Purpose']
    #
    #     uploads_data = {"loginuid": "", "logintoken": "","params": {"operation": "create", "title": "", "sourceName": "xx.mp4", "description": "xx","coverUrl": "xx", "tags": "xx"}}
    #     uploads_data['loginuid'] = self.user[0]
    #     uploads_data['logintoken'] = self.user[1]
    #     uploads_data['params']['title'] = self.user[0]
    #     uploads_data = json.dumps(uploads_data)
    #     print(uploads_data)
    #     result = json.loads(self.http.post(self.lib.webapi_url + 'index.php/video-upload/index', data=uploads_data))
    #     print(result)
    #     video_id = self.http.get_value(result, 'VideoId')
    #
    #     post_data = data['Request_Data']
    #     post_data = json.loads(post_data)
    #     post_data['loginuid'] = self.user[0]
    #     post_data['logintoken'] = self.user[1]
    #     post_data['params']['videoID'] = video_id
    #     post_data['params']['content'] = 'shipin'
    #     print(post_data)
    #     result = json.loads(self.http.post(self.lib.webapi_url + data['Request_URL'], data=post_data))
    #     # self.assertEqual(data['Check_Point'], self.http.get_value(result, 'info'))
    #     print(result)

    @ddt.data(*data[7:8])
    def test1_create_dynamic_video_is_ok(self, data):
        ''' 发布视频帖 '''

        self.case_name = data['API_Purpose']
        uploads_data = {"loginuid":"","logintoken":"","params":{"operation":"create","title":"","sourceName":"xx.mp4","description":"xx","coverUrl":"xx","tags":"xx"}}
        uploads_data['loginuid'] = self.user[0]
        uploads_data['logintoken'] = self.user[1]
        uploads_data['params']['title'] = self.user[0]
        uploads_data = json.dumps(uploads_data)
        print(uploads_data)
        result = json.loads(self.http.post(self.lib.webapi_url + '', data=uploads_data))
        print(result)
