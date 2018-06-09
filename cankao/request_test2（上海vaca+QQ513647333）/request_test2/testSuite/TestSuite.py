#!/usr/bin/env python3
#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'vaca'
__description__:'运行所有开启的测试用例并选择对应方法'
__mtime__:2017/6/10
'''

import time
import GetToken
import globalvariable
from readExcel import ReadExcel
from TestCase1 import TestCase1
from TestCase2 import TestCase2
from TestXlsxReport import Report
from log import Log

ReadExcel = ReadExcel()
report = Report()
log = Log()
runcase = 2

class TestAllCase:
    def __init__(self):
        # 从excel提取测试用例信息
        self.rows = ReadExcel.get_rows()
        self.running = ReadExcel.get_col(9)
        self.function_method = ReadExcel.get_col(10)

    def test_01case(self, token, worksheet):
        '''运行excel里所有符合TestCase1方法且需运行的case'''
        global runcase
        for row in range(1, self.rows):
            if self.function_method[row] == 1.0 and self.running[row] == "Yes":
                runcase += 1
                TestCase1(row).test_case1(token, worksheet, runcase)
                log.info('*' * 100)

    def test_02case(self, token, worksheet):
        '''运行excel里所有符合TestCase2方法且需运行的case'''
        global runcase
        for row in range(1, self.rows):
            if self.function_method[row] == 2.0 and self.running[row] == "Yes":
                runcase += 1
                TestCase2(row).test_case2(token, worksheet, runcase)
                log.info('*' * 100)
        report.close_workbook()


def main():
    log.info('开始测试')
    start = time.time()
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start))
    log.info('当前时间是：%s' % start_time)
    report.test_detail()
    report.init()
    sheet2 = report.get_sheet2()
    token = GetToken.GetToken().get_token()
    TestAllCase().test_01case(token, sheet2)
    TestAllCase().test_02case(token, sheet2)
    end = time.time()
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end))
    log.info('当前时间是：%s' % end_time)
    log.info('耗时：%s' %(end - start))
    log.info('测试完毕')
if __name__ == '__main__':
    main()
