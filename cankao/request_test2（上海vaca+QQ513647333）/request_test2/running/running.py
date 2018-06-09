#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'vaca'
__description__:'运行测试框架'
__mtime__:2017/6/10
'''
import time

import TestRequest
import TestSuite
from GetToken import GetToken
from TestAllRunner import TestAllRunner
from TestXlsxReport import Report
from log import Log
from sendEmail import SendEmail

report = Report()
log = Log()
sendemail = SendEmail()


class Running:
    def __init__(self):
        self.sheet = report.get_sheet()

    def write_data(self, runcase, passcase, failcase, pass_rate, time):
        '''
        把case统计数据写入excel
        runcase: 运行的用例数
        passcase: 通过的用例数
        failcase: 失败的用例数
        pass_rate: 通过率
        time: 耗时
        '''
        report.write_cell(self.sheet, 'E3', runcase)
        report.write_cell(self.sheet, 'E4', passcase)
        report.write_cell(self.sheet, 'E5', failcase)
        report.write_area(self.sheet, "F4:F6", time, 's')
        report.write_area(self.sheet, "G4:G6", pass_rate, '%')

    def running(self):
        '''运行测试框架'''
        log.info('开始测试')
        start = time.time()
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start))
        log.info('当前时间是：%s' % start_time)
        # 生成模板报告
        report.test_detail()
        report.init()
        # 运行用例
        token = GetToken().get_token()
        sheet2 = report.get_sheet2()
        TestAllRunner().threads(token, sheet2)
        end = time.time()
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end))
        log.info('当前时间是：%s' % end_time)
        # 获取用例统计数据并写入
        runcase = TestSuite.runcase - 2
        passcase = TestRequest.passcase
        failcase = runcase - passcase
        pass_rate = (passcase / runcase) * 100
        self.write_data(runcase, passcase, failcase, pass_rate, end - start)
        report.close_workbook()
        # 发送邮件
        report_address = report.get_workaddress()
        sendemail.sendmail(report_address)
        log.info('测试完毕')


def main():
    Running().running()
if __name__ == '__main__':
    main()
