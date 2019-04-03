"""
@Name: test_user_register
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/8/27
"""

import json
import unittest

import ddt

from lib.web.business import BusinessApi
from lib.web.client import HttpHandler
from config.ReadExcel import ExcelData
from config.cnf import Config
from config.mysql import MysqlData

data= ExcelData('appapi').readData()

@ddt.ddt
class TestAppApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http = HttpHandler()
        cls.lib = BusinessApi()
        cls.mysql = MysqlData()
        cls.config = Config()
        cls.num_start = ['130','131','132','133','134','135','136','137','138','139','145','146','147','148','149','150','151','152','153','155','156','157','158','159','165','166','171','172','173','174','175','176','177','178','180','181','182','183','184','185','186','187','188','189','191','198','199']


    @ddt.data(*data[0:11])
    def test1_check_name_is_ok(self, data):
        ''' 不合法的用户名校验 '''
        post_data = data['Request_Data']
        post_data = post_data.encode('utf-8')
        result = json.loads(self.http.post(self.lib.appapi_url + data['Request_URL'], data=post_data))
        self.case_name = data['API_Purpose']
        self.assertEqual(data['Check_Point'], self.http.get_value(result, 'info'))

    @ddt.data(*data[11:16])
    def test2_check_name_is_ok(self, data):
        ''' 合法的用户名校验 '''
        post_data = data['Request_Data']
        post_data = post_data.encode('utf-8')
        result = json.loads(self.http.post(self.lib.appapi_url + data['Request_URL'], data=post_data))
        self.case_name = data['API_Purpose']
        self.assertEqual(data['Check_Point'], self.http.get_value(result, 'info'))

    @ddt.data(*data[16:27])
    def test3_check_phone_is_ok(self, data):
        ''' 不合法的手机号校验 '''
        post_data = data['Request_Data']
        post_data = post_data.encode('utf-8')
        result = json.loads(self.http.post(self.lib.appapi_url + data['Request_URL'], data=post_data))
        self.case_name = data['API_Purpose']
        self.assertEqual(data['Check_Point'], self.http.get_value(result, 'info'))

    @ddt.data(*data[27:29])
    def test4_check_phone_is_ok(self, data):
        ''' 合法的手机号校验 '''
        post_data = data['Request_Data']
        post_data = post_data.encode('utf-8')
        result = json.loads(self.http.post(self.lib.appapi_url + data['Request_URL'], data=post_data))
        self.case_name = data['API_Purpose']
        self.assertEqual(data['Check_Point'], self.http.get_value(result, 'info'))

    @ddt.data(*data[29:30])
    def test5_check_phone_is_ok(self, data):
        ''' 手机号11位合法号段验证 '''
        post_data = data['Request_Data']
        self.case_name = data['API_Purpose']

        for item in self.num_start:
            phone = item + '12345678'
            post_data = json.loads(post_data)
            post_data['params']['name'] = phone
            post_data = json.dumps(post_data)
            result = json.loads(self.http.post(self.lib.appapi_url + data['Request_URL'], data=post_data))
            # print(result)
            try:
                self.assertEqual(data['Check_Point'], self.http.get_value(result, 'info'))
            except:
                self.assertEqual('手机号已存在！', self.http.get_value(result, 'info'))

    @ddt.data(*data[30:31])
    def test6_check_phone_is_ok(self, data):
        ''' 手机号11位不合法号段验证 '''
        post_data = data['Request_Data']
        self.case_name = data['API_Purpose']
        # num_start = ['100','101','102','103','104','105','106','107','108','109','110','111','112','113','114','115','116','117','118','119','120','121','122','123','124','125','126','127','128','129','140','141','142','143','144','154','160','161','162','163','164','167','168','169','170','179','190','192','193','194','195','196','197']

        for item in self.num_start:
            phone = item + '12345678'
            post_data = json.loads(post_data)
            post_data['params']['name'] = phone
            post_data = json.dumps(post_data)
            result = json.loads(self.http.post(self.lib.appapi_url + data['Request_URL'], data=post_data))
            print(phone + '\n')
            print(result)
            self.assertEqual(data['Check_Point'], self.http.get_value(result, 'info'))


