"""
@Name: tool
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/9
"""

import xlrd
from .config import Config


class ExcelData(Config):
    def __init__(self):
        super(ExcelData, self).__init__()
        self.read_config = Config()
        self.data_address = self.read_config.get_config('DATABASE', 'data_address')
        self.workbook = xlrd.open_workbook(self.data_address)
        self.table = self.data_address.sheet_by_name('Sheet1')

        # get titles
        self.row = self.table.row_values(0)

        # get rows number
        self.rowNum = self.table.nrows

        # get columns number
        self.colNum = self.table.ncols

        # the current column
        self.curRowNo = 1

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