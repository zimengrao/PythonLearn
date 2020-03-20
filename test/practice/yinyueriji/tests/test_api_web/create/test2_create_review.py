"""
@Name: test2_create_review.py
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2019/1/23
"""
import json
import unittest
import ddt

from lib.web.business import BusinessApi
from lib.web.client import HttpHandler
from config.RandomChinese import Random_Chinese
from config.ReadExcel import ExcelData
from config.cnf import Config
from config.mysql import MysqlData

data= ExcelData('cwebapi').readData()
# print(data)
@ddt.ddt
class HqsApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http = HttpHandler()
        cls.lib = BusinessApi()
        cls.mysql = MysqlData()
        cls.config = Config()
        cls.randomc = Random_Chinese()
        cls.user = cls.lib.get_token()

    @ddt.data(*data[0:1])
    def test1_create_dynamic_video_is_ok(self, data):
        ''' 发布视频帖评论 '''

        # self.case_name = '时代峻峰个'
        self.case_name = data['API_Purpose']
        self.detail_id = self.mysql.selectOne("SELECT tc092_dyna_short_id FROM `ceshihao3.6`.gt092_dynamic_short where tc092_type='7b9aa612-0446-d7ee-df05-477fdcc61831' and tc092_is_delete=2 order by tc092_id desc limit 1;")
        post_data = data['Request_Data']

        # for item in random_chinese=len(self.randomc.cre_name())
        post_data = json.loads(post_data)

        i = 0
        while i<=30:
            post_data['loginuid'] = self.user[0]
            post_data['logintoken'] = self.user[1]
            post_data['params']['detail_id'] = self.detail_id[0]
            random_chinese = self.randomc.cre_name()
            print(random_chinese)
            post_data['params']['content'] = random_chinese
            post_data1 = json.dumps(post_data)
            result = json.loads(self.http.post(self.lib.webapi_url + data['Request_URL'], data=post_data1))

            # self.assertEqual(data['Check_Point'], self.http.get_value(result, 'info'))
            print(result)
            i = i + 1
    # @ddt.data(*data[7:8])
    # def test1_create_dynamic_video_is_ok(self, data):
    #     ''' 发布视频帖 '''
    #
    #     self.case_name = data['API_Purpose']
    #     uploads_data = {"loginuid":"","logintoken":"","params":{"operation":"create","title":"","sourceName":"pc.mp4","description":"pc","coverUrl":"pc","tags":"pc"}}
    #     uploads_data['loginuid'] = self.user[0]
    #     uploads_data['logintoken'] = self.user[1]
    #     uploads_data['params']['title'] = self.user[0]
    #     uploads_data = json.dumps(uploads_data)
    #     print(uploads_data)
    #     result = json.loads(self.http.post(self.lib.webapi_url + '', data=uploads_data))
    #     print(result)
