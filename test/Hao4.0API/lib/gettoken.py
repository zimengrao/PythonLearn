"""
@Name: token
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/11
"""

import xlrd
from config.cnf import Config
import json

class ExcelData(Config):
    def __init__(self):
        super(ExcelData, self).__init__()
        self.config = Config()
        self.data_address = self.config.get_config('DATABASE', 'data_address')
        self.workbook = xlrd.open_workbook(self.data_address, 'utf-8')

    def readData(self, table_name):

        """

        :param table_name: 工作表名称
        :return: 以list返回每个工作表中的所有数据
        """
        self.table = self.workbook.sheet_by_name(table_name)
        self.row = self.table.row_values(0)  # 获取行title
        self.rowNum = self.table.nrows  # 获取行数量
        self.colNum = self.table.ncols  # 获取列数量
        self.curRowNo = 1  # the current column

        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r

    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1

        return r

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True

    def writeData(self,table_name):
        self.table = self.workbook.sheet_by_name(table_name)

