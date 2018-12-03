"""
@Name: test1
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/1/25
"""
import time
import json
from selenium import webdriver
from lxml.html import fromstring
# from selenium.webdriver.support.wait import webDriverWait

HOME_INPUT_SEARCh_XPATH = '//*[@id="vue-index"]/section/article/div[2]/div/div/input'
HOME_SEARCH_BUTTON_XPATH = '//*[@id="vue-index"]/section/article/div[2]/div/a[2]'
SEARCH_APP_LIST_XPATH = '//*[@title="{}"]'
class WebDriverClient:
    def __init__(self):
        #初始化一个浏览器
        self.driver = webdriver.Firefox()

    def check_elements(self, xpaths) -> bool:

        # 传递的xpath在当前界面是否存在，如果存在返回true，不存在返回False
        return bool(self.driver.find_element_by_xpath(xpaths))

    def parse(self, xpath):
        # page_source 是当前页面的源码
        # fromstring().xpath 的返回结果是xpath中元素的值
        return fromstring(self.driver.page_source).xpath(xpath)

    def click(self,xpath):
        # 过xpath定位单击按钮，点击
        self.driver.find_element_by_xpath(xpath).click()

    def send_keys(self, xpath, value):
        # 通过xpath定位输入框，将值传入输入框
        self.driver.find_element_by_xpath(xpath).send_keys(value)

    def retry(self, xpath):
        # 如果check_elements为true，进入while循环，如果不存在等待，等待5s后，抛出异常错误

        num = 0
        checker = None
        while 1:
            try:
                checker = self.check_elements(xpath)
                if checker:
                    return checker
            except Exception:
                print(self.parse(xpath))
            num += 1
            time.sleep(2)

    # def implicitly_wait(self, timeout = 10):
    #     self.driver.implicitly_wait(timeout)
    # def wait(self, local):

    def close(self):
    # 关闭浏览器
        self.driver.close()

class AndroidCoolChuan(WebDriverClient):


    def __init__(self, package = 'com.tencent.mm',appname = '微信'):
        super(AndroidCoolChuan, self).__init__() #初始化
        self.package = package
        self.appname =appname
        self.home_url = 'http://android.kuchuan.com/page/detail/index'
        self.all_data_url = 'http://android.kuchuan.com/dailydownload?packagename={}&status=-1&date={}'.format(self.package, int(time.time()* 1000))

    def get_appinfo_page(self):
        # 打开 网站
        # 输入搜索关键字
        # 单击搜索按钮
        #
        self.driver.get(self.home_url)
        self.send_keys(HOME_INPUT_SEARCh_XPATH, self.appname)
        time.sleep(2)
        self.click(HOME_SEARCH_BUTTON_XPATH)
        time.sleep(2)
        self.click(SEARCH_APP_LIST_XPATH.format(self.appname))
        time.sleep(2)

    def get_all_datas(self):
        self.get_appinfo_page()
        if self.retry('//*[@id="vue-download"]/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/h4/span/span'):
            self.driver.get(self.all_data_url)
            result = str(self.parse('//text()')[0])
            print(result, type(result))
            data_dict = json.loads(result) # json.loads 是把一个json结构体（是字符串类型的字典）转化成dict类型
            print(data_dict, type(data_dict))

    # def detail_version(self):
    #     time.sleep(5)
    #     self.driver.get('')

if __name__ == '__main__':
    wechat = AndroidCoolChuan()
    wechat.get_all_datas()
