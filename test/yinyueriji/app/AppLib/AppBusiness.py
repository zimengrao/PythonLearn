"""
@Name: AppBusiness
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/10/15
"""

from config.cnf import Config

class AppBusiness:
    def __init__(self):
        super(AppBusiness, self).__init__()
        self.config = Config()

    # def driver(self):
    #     self.driver = Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
    #     return self.driver


