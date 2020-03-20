"""
@Name: KuhuCode
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/1/25
"""

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)

if __name__=='__main__':
    p=Person('bob','male')
    # print(p)