"""
@Name: tool
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/9
"""

import shutil
import os
import xlrd
from xlutils.copy import copy
from config.cnf import Config

class WriteData(Config):
    def __init__(self, sheet):
        super(WriteData, self).__init__()
        self.address = Config().get_config('DATABASE', 'data')
        self.workbook = xlrd.open_workbook(self.address)
        self.workbook1 = copy(self.workbook)
        self.sheet = self.workbook1.get_sheet(sheet)


    def write(self, i, j, value):

        """
        :param i: 写入第几行，从第0行开始数
        :param j: 写入第几列，从第0列开始数
        :param value: 写入单元格值
        :return:
        """
        self.sheet.write(i,j,value)

    def save(self, book_name):
        '''
        保存写入的数据，并将写入的数据剪切到config文件夹下
        :param book_name:
        :return:
        '''
        self.workbook1.save(book_name)
        if os.path.exists('F:\\python\\PythonLearn\\test\\Hao4.0API\\config\\data.xls'):
            os.remove('F:\\python\\PythonLearn\\test\\Hao4.0API\\config\\data.xls')
        shutil.move(book_name, 'F:\\python\\PythonLearn\\test\\Hao4.0API\\config\\data.xls')


# if __name__ == '__main__':
#     f = WriteData()
#     f.write()