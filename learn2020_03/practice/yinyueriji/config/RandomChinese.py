# coding=utf-8
"""
@Name: RandomChinese
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2019/1/18
"""

import codecs
import random
from functools import reduce
import copy

# 经过山东菏泽王晓辉老师的提醒
# 随机名称还可以用汉字区位码
# 改进程序

# 知乎得到启发
# str = "\"\\u5c3c\\u5eb7\""
# str = codecs.decode(str,'unicode_escape')
# print(str)  #输出：尼康

# 根据gb2312生成随机字符串
class Random_Chinese:
    def random_gb2312_char(self):
        self.zone_num = random.randint(0xb0, 0xd7)
        self.bit_num = random.randint(0xa1, 0xff)
        # print(zone_num, bit_num)
        self.hex = format(self.zone_num, 'x') + format(self.bit_num, 'x')
        # bytes().fromhex(a)从十六进制生成字节
        # print(self.hex)

        return bytes().fromhex(self.hex).decode('gb2312')



    # 并非常用汉字范围，常用汉字没有特定的区间
    # 需要自行排出
    # 所以找出常用字然后随机生成也是个办法了
    # 至于那种方便就很难说了是

    def cre_name(self):
        # print(i)
        i = random.randint(4,101)
        # self.username = [''] * i
        self.username = ''
        print(i)
        t = 1
        try:
            while t < i:
                self.username = self.username + self.random_gb2312_char()
            # self.name = list(map(lambda x: x + self.random_gb2312_char(),self.username))
            # self.username = ''.join(list(self.name))
                t = t+1
            print(self.username)
            print(type(self.username))
            return self.username
        except:
            return None

    def content(self):
        while self.cre_name() == None:
            self.cre_name()
        return self.cre_name()
    # def num(self, i):
    #     for x in range(i):
    #
    #         return cre_names

#
if __name__ == '__main__':
    dd=Random_Chinese()
    dd.cre_name()
    # i = 1
    # while i < 50:
    #     dd.cre_name()
    #     print(i)
    #     i = i +1


# for x in range(10):
#     print(cre_name())
# 进一步改进是找到常用汉字的编码
# 或者不用Unicode码而用表示汉字比较少的编码

# random_gb2312_char()

# cre_name()