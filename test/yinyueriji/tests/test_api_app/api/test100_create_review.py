"""
@Name: test100_create_review
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2019/1/18
"""

import json
import unittest

import ddt

from lib.web.business import BusinessApi
from lib.web.client import HttpHandler
from config.ReadExcel import ExcelData
from config.cnf import Config
from config.mysql import MysqlData

data= ExcelData('create').readData()

@ddt.ddt
class HqsApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http = HttpHandler()
        cls.lib = BusinessApi()
        cls.mysql = MysqlData()
        cls.config = Config()

    @ddt.data(*data[1:2])
    def test1_create_review_is_ok(self, data):
        ''' 视频帖发布评论 '''

        post_data = data['Request_Data']
        data_utf8 = post_data.encode('utf-8')
        self.case_name = data['API_Purpose']
        self.detail_id=list(self.mysql.selectOne("SELECT tc092_dyna_short_id FROM `ceshihao3.6`.gt092_dynamic_short where tc092_type='7b9aa612-0446-d7ee-df05-477fdcc61831' and tc092_is_delete=2 order by tc092_id desc limit 1;"))

        # print(self.detail_id)
        login = list(self.lib.get_token())
        print(login[0])
        print(login[1])
        data_utf8['loginuid'] = str(login[0])
        data_utf8['logintoken'] = str(login[1])
        # data_utf8['params']['detail_id']='56112915-60c5-29db-df37-bedb9e93239d'
        data_utf8['params']['detail_id']=str(self.detail_id[0])
        data_utf8['params']['content']= '发布评论测试'
        result = json.loads(self.http.post(self.lib.appapi_url + data['Request_URL'], data=data_utf8))
        # self.assertEqual(data['Check_Point'], self.http.get_value(result, 'info'))
        print(result)
    #
    #
    # @ddt.data(*data[35:37])
    # def test5_check_login_is_ok(self, data):
    #     ''' 登录成功验证 '''
    #     post_data = data['Request_Data']
    #     post_data = post_data.encode('utf-8')
    #     result = json.loads(self.http.post(self.lib.appapi_url + data['Request_URL'], data=post_data))
    #     self.case_name = data['API_Purpose']
    #     self.assertEqual(data['Check_Point'], self.http.get_value(result, 'info'))
    #     print(result)
