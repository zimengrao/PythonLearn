#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'vaca'
__description__:'处理有token和data且不需要转换json数据的case,并写入excel'
__mtime__:2017/6/12
'''

import ast
import GetToken     # 测试脚本
import globalvariable
from readConfig import ReadConfig
from readExcel import ReadExcel
from TestRequest import TestRequest
from TestXlsxReport import Report
from log import Log

ReadConfig = ReadConfig()
ReadExcel = ReadExcel()
TestRequest = TestRequest()
report = Report()
log = Log()


class TestCase2:
    def __init__(self, rownum=None):
        '''
            rownum: 读取excel的行数
        '''
        self.actual = {}
        # 从config.ini提取数据
        self.hostname = ReadConfig.get_config("DATABASE", "hostname")
        self.code = ReadConfig.get_config("DATABASE", "code")
        # 从excel提取测试用例信息
        self.testcassid = ReadExcel.get_cell(rownum, globalvariable.CASE_ID)
        self.testcassname = ReadExcel.get_cell(rownum, globalvariable.CASE_NAME)
        self.url_path = ReadExcel.get_cell(rownum, globalvariable.CASE_URL)
        self.method = ReadExcel.get_cell(rownum, globalvariable.CASE_METHOD)
        self.headers = ReadExcel.get_cell(rownum, globalvariable.CASE_HEADERS)
        self.hope = ReadExcel.get_cell(rownum, globalvariable.CASE_CODE)
        self.data = ReadExcel.get_cell(rownum, globalvariable.CASE_DATA)

    def test_case2(self, token, worksheet, temp):
        '''处理有token和data且不需要转换json数据的case'''
        url = self.hostname + self.url_path
        data_dict = ast.literal_eval(self.data)     # 转换数据成字典
        log.debug('data的数据类型是：%s' % type(data_dict))
        data_dict["token"] = token
        if self.method == "POST":
            log.debug('使用%s方法执行用例%s' % (self.method, self.testcassid))
            try:
                self.actual = TestRequest.testpostreuqest(url, data_dict, self.headers, self.testcassid,
                                                          self.testcassname, self.hope)
                log.debug('用例%s执行完毕' % self.testcassid)
            except Exception:
                log.error('参数缺失')
            finally:
                report.write_basic(self.testcassid, self.testcassname, self.method, self.hope, url, data_dict,
                                   worksheet, temp)
                log.info("基本数据写入成功")
            report.write_special(self.actual, self.hope, worksheet, temp)
            log.debug("特殊数据写入成功")
        elif self.method == "GET":
            log.debug('使用%s方法执行用例%s' % (self.method, self.testcassid))
            try:
                self.actual = TestRequest.testgetrequest(url, data_dict, self.headers, self.testcassid,
                                                         self.testcassname, self.hope)
                log.debug('用例%s执行完毕' % self.testcassid)
            except Exception:
                log.error('参数缺失')
            finally:
                report.write_basic(self.testcassid, self.testcassname, self.method, self.hope, url, data_dict,
                                   worksheet, temp)
                log.debug("基本数据写入成功")
            report.write_special(self.actual, self.hope, worksheet, temp)
            log.debug("特殊数据写入成功")
        else:
            report.write_basic(self.testcassid, self.testcassname, self.method, self.hope, url, data_dict,
                               worksheet, temp)
            report.write_cell(worksheet, "G%s" % temp, "调用方法错误")
            report.write_cell(worksheet, "H%s" % temp, "失败")
            log.error('没有%s对应的方法%s' % (self.testcassid, self.method))
        report.close_workbook()

def main():
    report.test_detail()
    report.init()
    sheet2 = report.get_sheet2()
    token = GetToken.GetToken().get_token()
    test = TestCase2(5)
    test.test_case2(token, sheet2, 3)
if __name__ == '__main__':
    main()