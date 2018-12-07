
"""
@Name: ooo.py
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/12/3
"""


class Parent(object):
    a = 0
    b = 1

    def __init__(self):
        self.a = 2
        self.b = 3

    def p_test(self):
        pass


class Child(Parent):
    a = 4
    b = 5

    def __init__(self):
        super(Child, self).__init__()
        # self.a = 6
        # self.b = 7

    def c_test(self):
        pass

    def p_test(self):
        pass


p = Parent()
c = Child()
print(Parent.__dict__)
print(Child.__dict__.get('p_test'))
print(Child.__dict__)
print(c.__dict__)