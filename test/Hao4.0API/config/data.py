"""
@Name: tool
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/9
"""

import xlrd
from config.cnf import Config
# import json
import xlwt
from xlutils.copy import copy
# table_name = 'Sheet1'

class ExcelData(Config):
    def __init__(self):
        super(ExcelData, self).__init__()
        self.config = Config()
        self.data_address = self.config.get_config('DATABASE', 'data_address')
        self.workbook = xlrd.open_workbook(self.data_address, 'utf-8')
        self.workbook1 = xlwt.Workbook(self.data_address)
        self.workbook2 = xlrd.open_workbook(self.data_address)


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

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True

    def writeData(self, i ,j, data):
        sheet1 = self.workbook1.add_sheet('user', cell_overwrite_ok=True)
        sheet1.write(i, j, data)
        self.workbook1.save('user_data.xls')


# if __name__ == '__main__':
#     f = ExcelData()
#     f.writeData()