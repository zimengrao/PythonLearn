#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'vaca'
__description__:'获取接口返回数据'
__mtime__:2017/6/10
'''

import requests
import json
from log import Log

log = Log()
passcase = 0


class TestRequest:
    def testpostreuqest(self, url, data, headers, testcassid, testcassname, hope):
        '''获取post方法返回的数据
            url: 接口地址
            data: 请求参数
            headers: 请求头
            testcassid: 用例ID
            testcassname: 用例名称
            hope: 预期code
        '''
        global passcase
        hr = requests.post(url, data=data, headers=headers)
        json_data = json.loads(hr.text)  # 获取并处理返回的json数据
        if hope == json_data['resCode']:
            passcase += 1
            log.info('测试用例ID：%s' % testcassid)
            log.info('测试用例名称：%s' % testcassname)
            log.debug('测试通过')
            log.debug('测试返回数据：%s' % json_data)
            log.info("返回的消息是：%s" % json_data['resDesc'])
        else:
            log.info('测试用例ID：%s' % testcassid)
            log.error('测试用例名称：%s' % testcassname)
            log.error('测试失败')
            log.error('测试返回数据：%s' % json_data)
            log.error("返回的消息是：%s" % json_data['resDesc'])
        return json_data

    def testgetrequest(self, url, data, headers, testcassid, testcassname, hope):
        '''获取get方法返回的数据
            url: 接口地址
            data: 请求参数
            headers: 请求头
            testcassid: 用例ID
            testcassname: 用例名称
            hope: 预期code
        '''
        global passcase
        hr = requests.get(url, params=data, headers=headers)
        json_data = json.loads(hr.text)
        if hope == json_data['resCode']:
            passcase += 1
            log.info('测试用例ID：%s' % testcassid)
            log.info('测试用例名称：%s' % testcassname)
            log.debug('测试通过')
            log.debug('测试返回数据：%s' % json_data)
            log.info("返回的消息是：%s" % json_data['resDesc'])
        else:
            log.info('测试用例ID：%s' % testcassid)
            log.error('测试用例名称：%s' % testcassname)
            log.error('测试失败')
            log.error('测试返回数据：%s' % json_data)
            log.error("返回的消息是：%s" % json_data['resDesc'])
        return json_data


def main():
    a = 1
    # token = GetToken.GetToken().get_token()
    # TestCase1.TestCase1(2).test_case1(token)
if __name__ == '__main__':
    main()
