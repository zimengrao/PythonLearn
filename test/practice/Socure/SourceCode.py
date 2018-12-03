"""
@Name: SourceCode
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/1/2
"""

from requests import Session
from lxml import etree

class BaseCrawl:
    def __init__(self):
        self.session = Session()

    def request(self, url, encoding='utf-8'):
        resp = self.session.get(url)
        if resp.encoding != encoding:
            resp.encoding = encoding
        return resp

    def parse(self, html, xpaths):
        selector = etree.HTML(html)
        if isinstance(xpaths, (tuple, list)):
            return [selector.xpath(xpath) for xpath in xpaths]
        return selector.xpath(xpaths)

    def output(self, url, xpaths, content=None):
        resp = self.request(url)
        html = resp.content if content else resp.text
        return self.parse(html, xpaths)

class TesterHomeCrawl(BaseCrawl):
    def __init__(self):
        super(TesterHomeCrawl, self).__init__()
        self.home_page_url = 'https://testerhome.com/'

    def get_all_default_module(self):
        resp = self.output(self.home_page_url, '//*[@class="home_suggest_topics panel panel-default"]')
        for item in resp:
            all_title = item.xpath('div["@class=panel-heading"]/text()')[0].strip()
            print('=======首页模块名称=======：{}'.format(all_title))
            for title in item.xpath('div/div[@class="col-md-6"]/div/div[@class="infos media-body"]/div/a/@title'):
                print('文章标题：', title)
            for topic in item.xpath('div[2]/div[@class="col-md-6 topics-group"]/div/div[2]/div/a/@title'):
                print('精华文章标题：', topic)
            for top in item.xpath('div[@class="panel-body"]/div/div/a/@title'):
                print('{}:{}'.format(all_title, top))

    def get_testerhome_tags(self):
        resp = self.output(self.home_page_url, '//*[@class="nav navbar-nav"]/li/a')
        for item in resp:
            # print('=============={}=============='.format(item.xpath('text()')))
            print('=============={}=============='.format(item.xpath('text()')[0]))
            resp = self.output(self.home_page_url + item.xpath('@href')[0], '//*[@class="infos media-body"]')
            for info in resp:
                title = info.xpath('div[1]/a/@title')
                # print(title)
                user = info.xpath('div[2]/a/@data-name')
                # print(title[0], user[0])
                last_user_name = info.xpath('div[2]/span/a/@data-name')
                if last_user_name and user:
                    print(title, user[0], last_user_name[0])

    def get_opensource_projectd(self):
        url = 'https://testerhome.com/opensource_projects'
        resp = self.output()


if __name__ == '__main__':
    tester = TesterHomeCrawl()
    # tester.get_all_default_module()
    tester.get_testerhome_tags()