"""
@Name: business
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/9
"""
import json

from config.excelData import ExcelUtil
from .client import HttpHandler


class BusinessApi(HttpHandler):
    def __init__(self):
        super(BusinessApi, self).__init__()
        self.excel = ExcelUtil
        self.http = HttpHandler
        global excel
        excel = self.excel(excel_path, excel_name)

    def excel_data(self, excel_path, excel_name):
        self.excel = self.excel(excel_path, excel_name)
        return self.excel


    def login_value(self):
        resp = json.loads(self.post(base_url, da))
