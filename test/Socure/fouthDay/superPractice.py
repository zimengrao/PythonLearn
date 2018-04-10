#!/usr/bin/env python
# encoding: utf-8
'''
@author: wang'min
@Project:LearningPython
@file: 1.test.py
@time: 2017/12/18 15:25
'''

from selenium import webdriver
from lxml.html import fromstring
import time
import random

# class WebDriverClient:
#     """pass"""
#     def __int__(self):
#         self.driver = webdrvier.firefox()
#
#     def click(self, xpath):
#         self.driver.find_element_by_xpath(xpath).click()
#
#     def send_keys(self, xpath, vlaue):
#         self.driver.find_element_by_xpath(xpath).send_keys(value)
#
#     def parse(self, xpath):
#         html = self.driver.page_soure.replace().replace()
#         return fromstring(html).xpath(xpath)
#
#     def check(self, xpath):
#         return bool(self.parse(xpath))
#
#     # def get(self, url):
#     #     self.driver.get(url)
#
# class JanDan(WebDriverClient):
#     def __int__(self):
#         super(JanDan, self).__int__()
#         self.all_img_urls = 'http://baidu.com'
#         self.input_xpath = '//*[@id="kw"]'
#         self.click_xpath = '//*[@id="su"]'
#         self.titles_xpath = '//h3[@class="t"]/a'
#
#     def run(self):
#         n = 0
#         self.get(self.all_img_urls)
#         self.send_keys(self.input_xpath, '妹子图')
#         self.click(self.click_xpath)
#         while n < 11:
#             n += 1
#             time.sleep(1)
#             for item in self.parse(self.titles_xpath):
#                 print(item.xpath('text()'), item.xpath('@href'))
#             self.click('//a[text()="下一页"]')
#         self.driver.close()
#     def meizitu(self):
#         urls = ['http://jandan.net/ooxx/page-{}#comments'.format(num) for num in range(1, 378)]
#         for url in urls:
#             self.get(url)
#             time.sleep(random.randint(2, 5))
#             print(self.parse('//p/img/@src'))
#
# if __name__ == '__main__':
#     jd = JanDan()
#     jd.meizitu()
#
#
# a = 14
# if not type(a) == str:
#     raise AssertionError('a不是一个字符串')

# class FooParent(object):
#     def __init__(self):
#         #
#         self.parent = 'I\'m the parent.'
#         print('Parent')
#
#     def bar(self, message):
#         print("%s from Parent" % message)
#
#
# class FooChild(FooParent):
#     def __init__(self):
#         # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
#         super(FooChild, self).__init__()
#         print('Child')
#
#     def bar(self, message):
#         super(FooChild, self).bar(message)
#         print('Child bar fuction')
#         print(self.parent)
#
#
# if __name__ == '__main__':
#     fooChild = FooChild()
#     fooChild.bar('HelloWorld')


class A:
    def __init__(self):
        print('This is init function of A')

class B:
    def __init__(self):
        print('This is init function of B')
        super().__init__()

class C(B,A):
    pass

c = C()

print(type(C))
print(C.mro())