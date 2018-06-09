#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'vaca'
__description__:'处理只有token且不需要转换json数据的case,并写入excel'
__mtime__:2017/6/12
'''

import GetToken     # 测试脚本
import globalvariable
from readConfig import ReadConfig
from readExcel import ReadExcel
from TestRequest import TestRequest
from log import Log
from TestXlsxReport import Report

ReadConfig = ReadConfig()
ReadExcel = ReadExcel()
TestRequest = TestRequest()
report = Report()
log = Log()


class TestCase1():
    def __init__(self, rownum=None):
        '''
            rownum: 读取excel的行数
        '''

        self.actual = {}
        # 从config.ini提取数据
        self.hostname = ReadConfig.get_config("DATABASE", "hostname")

        # 从excel提取测试用例信息
        self.testcassid = ReadExcel.get_cell(rownum, globalvariable.CASE_ID)
        self.testcassname = ReadExcel.get_cell(rownum, globalvariable.CASE_NAME)
        self.url_path = ReadExcel.get_cell(rownum, globalvariable.CASE_URL)
        self.method = ReadExcel.get_cell(rownum, globalvariable.CASE_METHOD)
        self.headers = ReadExcel.get_cell(rownum, globalvariable.CASE_HEADERS)
        self.hope = ReadExcel.get_cell(rownum, globalvariable.CASE_CODE)

    def test_case1(self, token, worksheet, temp):
        '''运行只有token参数且不转换json数据的case'''
        url = self.hostname + self.url_path
        data = {
            "token":  token
        }
        if self.method == "POST":
            log.debug('使用%s方法执行用例%s' % (self.method, self.testcassid))
            try:
                self.actual = TestRequest.testpostreuqest(url, data, self.headers, self.testcassid, self.testcassname,
                                                          self.hope)
                log.debug('用例%s执行完毕' % self.testcassid)
            except Exception:
                log.error('参数缺失')
            finally:
                report.write_basic(self.testcassid, self.testcassname, self.method, self.hope, url, data, worksheet,
                                   temp)
                log.info("基本数据写入成功")
            report.write_special(self.actual, self.hope, worksheet, temp)
            log.debug("特殊数据写入成功")
        elif self.method == "GET":
            log.debug('使用%s方法执行用例%s' % (self.method, self.testcassid))
            try:
                self.actual = TestRequest.testgetrequest(url, data, self.headers, self.testcassid, self.testcassname,
                                                         self.hope)
                log.debug('用例%s执行完毕' % self.testcassid)
            except Exception:
                log.error('参数缺失')
            finally:
                report.write_basic(self.testcassid, self.testcassname, self.method, self.hope, url, data, worksheet,
                                   temp)
                log.debug("基本数据写入成功")
            report.write_special(self.actual, self.hope, worksheet, temp)
            log.debug("特殊数据写入成功")
        else:
            report.write_basic(self.testcassid, self.testcassname, self.method, self.hope, url, data, worksheet,
                               temp)
            report.write_cell(worksheet, "G%s" % temp, "调用方法错误")
            report.write_cell(worksheet, "H%s" % temp, "失败")
            log.error('没有%s对应的方法%s' % (self.testcassid, self.method))
        report.close_workbook()


def main():
    report.test_detail()
    report.init()
    sheet2 = report.get_sheet2()
    token = GetToken.GetToken().get_token()
    test = TestCase1(1)
    test.test_case1(token, sheet2, 3)
if __name__ == '__main__':
    main()