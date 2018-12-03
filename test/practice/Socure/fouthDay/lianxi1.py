"""
@Name: SourceCode.py
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/1/19
"""

from requests import Session
from lxml import etree
from selenium import webdriver
import time


# class BaseCrawl:
#     def __init__(self):
#         self.session = Session()
#         self.etree = etree
#
#     def  request(self, url, encoding = 'utf-8'):
#         resp = self.session.get(url)
#         if resp.encoding != encoding:
#             resp.encoding = encoding
#         return resp
#
#     def parse(self, html, xpaths):
#         selector = self.etree.HTML(html)
#         if isinstance(xpaths, (tuple, list)):
#             return [selector.xpath(xpath) for xpath in xpaths]
#         return selector.xpath(xpaths)
#
#     def output(self, url, xpath, content=None):
#         resp = self.request(url)
#         if content:
#             html = self.parse(resp.content, xpath)
#         return self.parse(resp.text, xpath)
#
# class TesterLifeCrawl(BaseCrawl):
#     def __init__(self):
#         super(TesterLifeCrawl, self).__init__()
#         self.url = 'http://testerlife.com/'
#         self.html = self.request(self.url).text
#
#     def get_titles(self):
#         elements = self.output(self.url, '//*[@class="article-header"]')
#         for element in elements:
#             print(element.xpath('h1/a/text()')[0], self.url + element.xpath('h1/a/@href')[0])
#
#     def get_article_inner(self):
#         elements = self.parse(self.html, '//*[@class="article-inner"]')
#         for element in elements:
#             article_title = element.xpath('header/h1/a/text()')
#             article_info = element.xpath('div/blockquote/p/text()')
#             article_tag = element.xpath('div[2]/div/ul/li/a/text()')
#             print(article_title, article_info, article_tag)
#
#     def get_all_plugin_tags(self):
#         elements = self.parse(self.html, '//*[@class="header-nav"]/ul/a/text()')
#         for element in elements:
#             print(element)

# driver = webdriver.Firefox()
# driver.get('https://www.baidu.com/')
# driver.close()

LOGIN_URL = 'https://testerhome.com/account/sign_in'
USER_NAME = 'zimengrao'
PASSWORD = 'wwMM258134679'
LOGIN_TESTERHOME_USERNAME_XPATHS = '//input[@id="user_login"]'
LOGIN_TESTERHOME_PASSWORD_XPATHS = '//input[@id="user_password"]'
LOGIN_TESTERHOME_BUTTON_XPATHS = '//input[@value="登录"]'
LOGIN_USER_NAME_XPATHS = '/html/body/div[1]/nav/div/ul[1]/li/ul/li[1]/a/text()'

SETTING_PAGE_URL = 'https://testerhome.com/setting'
SETTING_PAGE_USER_EMAIL_XPATHS = '//*[@name="user[email]"]'

class WebDriverClient:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.etree = etree.HTML

    def check_elements(self, xpath) -> bool:
        """
            判断传递进来的xpath对象，在driver的页面中是否存在
        :param xpath:
        :return:
        """
        return bool(self.driver.find_elements_by_xpath(xpath))

    def retry(self,xpath):
        """
            判断是否获取到登录后的xpath，未获取到等待
        :param xpath:
        :return:
        """
        retry_number = 0
        while not self.check_elements(xpath):
            time.sleep(1)
            print(retry_number)
            if retry_number == 5:
                raise AssertionError('Xpath中指定的元素不存在')

    def click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def send_keys(self, xpath, value):
        self.driver.find_element_by_xpath(xpath).send_keys(value)

    def driver_close(self):
        self.driver.close()

    def check_element_text(self, xpath):
        html = self.driver.page_source
        result = self.etree(html).xpath(xpath)[0]
        return result

class UiTestClass(WebDriverClient):

    def __init__(self):
        super(UiTestClass, self).__init__()

    def login(self):
        self.driver.get(LOGIN_URL)
        self.send_keys(LOGIN_TESTERHOME_USERNAME_XPATHS, USER_NAME)
        self.send_keys(LOGIN_TESTERHOME_PASSWORD_XPATHS, PASSWORD)
        self.click(LOGIN_TESTERHOME_BUTTON_XPATHS)


    def check_login_user_name(self):
        self.login()
        if not self.retry(LOGIN_USER_NAME_XPATHS):
            assert self.check_element_text(LOGIN_USER_NAME_XPATHS) == 'zimengrao'
        self.driver_close()

    def check_user_setting_page(self):
        self.login()
        time.sleep(2)
        self.driver.get(SETTING_PAGE_URL)
        if self.retry(SETTING_PAGE_USER_EMAIL_XPATHS):
            assert self.check_elements(SETTING_PAGE_USER_EMAIL_XPATHS) is True
        self.driver_close()

if __name__ == '__main__':

    uitest = UiTestClass()
    uitest.check_login_user_name()

    # driver = webdriver.Firefox()
    # driver.maximize_window()
    # #初始化一个浏览器窗口
    # #chrome driver
    # #firefox driver
    # #无UI界面的 phantomjs driver
    #
    # driver.get('https://testerhome.com/account/sign_in')
    # #去请求http://testerlife.com/account/sign_in
    #
    # driver.find_element_by_xpath('//input[@id="user_login"]').send_keys('zimengrao')
    # driver.find_element_by_xpath('//input[@id="user_password"]').send_keys('wwMM258134679')
    # driver.find_element_by_xpath('//input[@value="登录"]').click()
    # time.sleep(10)
    #
    # html = driver.page_source
    # # 把driver当前页面的源码赋值给html这个变量
    # assert_text = etree.HTML(html).xpath('/html/body/div[1]/nav/div/ul[1]/li/ul/li[1]/a/text()')
    # print(assert_text)
    # driver.close()
    #

    # assert_text = etree.HTML(html).xpath

    # testerhome = UiTestClass()
    # testerhome.get_testerlife_blog_title()

#     tester = TesterLifeCrawl()
#     tester.get_titles()
#     tester.get_article_inner()
#     tester.get_all_plugin_tags()
