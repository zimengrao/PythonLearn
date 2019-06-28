"""
@Name: tes
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2019/6/25
"""

class  DataTest:
    day = 0
    month = 0
    year = 0
    def __init__(self, year=0, month=0, day=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_date(cls, data_ad_string):
        # 处理构造函数中的数据
        year,month,day = map(int,data_ad_string.split('-'))
        date = cls(year, month, day)
        return date

    def out_date(self):
        print("year:{}".format(self.year))
        print("month:{}".format(self.month))
        print("day:{}".format(self.day))


class A:
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)
print(A.foo,'\n',A.class_foo,'\n',A.static_foo)

# t=DataTest.get_date('2019-6-25')
# t.out_date()