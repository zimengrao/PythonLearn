"""
@Name: 111
@Version:
@Project: PyCharm
@Author: wangmin
@Data: 2019/1/18
"""

import codecs
import random
from functools import reduce

# 经过山东菏泽王晓辉老师的提醒
# 随机名称还可以用汉字区位码
# 改进程序

# 知乎得到启发
# str = "\"\\u5c3c\\u5eb7\""
# str = codecs.decode(str,'unicode_escape')
# print(str)  #输出：尼康

# 根据gb2312生成随机字符串
def random_gb2312_char():

    zone_num = random.randint(0xb0, 0xd7)
    bit_num = random.randint(0xa1, 0xff)
    # print(zone_num, bit_num)
    hex = format(zone_num, 'x') + format(bit_num, 'x')
    # bytes().fromhex(a)从十六进制生成字节
    # print(hex)

    return bytes().fromhex(hex).decode('gb2312')



# 并非常用汉字范围，常用汉字没有特定的区间
# 需要自行排出
# 所以找出常用字然后随机生成也是个办法了
# 至于那种方便就很难说了是
def cre_name():
    i = random.randint(1, 90)
    # print(i)
    username = [''] * i
    print(lambda x : x + random_gb2312_char(), username)
    name = map(lambda x : x + random_gb2312_char(), username)
    # print(name)
    username = ''.join(list(name))
    # print(username)
    return username

# for x in range(10):
#     print(cre_name())
# 进一步改进是找到常用汉字的编码
# 或者不用Unicode码而用表示汉字比较少的编码

# random_gb2312_char()

cre_name()