#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'vaca'
__description__:'创建多线程(貌似没用)'
__mtime__:2017/6/8
'''

import time
import threading
import GetToken     # 测试脚本
from TestSuite import TestAllCase
from TestXlsxReport import Report
from log import Log
log = Log()
report = Report()


class TestAllRunner:
    def threads(self,token, worksheet):

        hthreads = []  # 创建线程数组
        # 定义线程
        hthreads.append(threading.Thread(target=TestAllCase().test_01case(token,worksheet)))
        hthreads.append(threading.Thread(target=TestAllCase().test_02case(token,worksheet)))
        # 读取数组内的所有线程，并同时执行
        for h in hthreads:
            h.start()  # 开始线程活动
            h.join()  # 把主线程挂起，等待上面的线程跑完了在运行
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
    TestAllRunner().threads(token, sheet2)
    report.close_workbook()
    end = time.time()
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end))
    log.info('当前时间是：%s' % end_time)
    log.info('耗时：%s' % (end - start))
    log.info('测试完毕')
if __name__ == '__main__':
    main()
