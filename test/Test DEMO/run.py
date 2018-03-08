"""
@Name: run
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/2/1
"""

"""
1、lib中间插件，每个lib模块下都要有__init__.py；如果用python package会自带此问文件
2、tests所有的case放在这个路径下
3、report测试报告放在这个路径下
4、run.py 通过unitest去load下所有指定路径下的case，把程序执行起来; 启动器
"""

# root path 是TestDemo这个文件下的路径
# 如果需要引入package 或module的工具类或者模块， 引入层级的第一级为root path
# 如果tests文件夹需要load lib和config文件下的文件，必须有__init__.py文件

# 1、driver 句柄
# 2、classmethod

"""
1、类下面的每一方法只做一个功能，比如说click、截图等
2、原子化层级：WebDiverClient，config；
   业务封装层级：page object，Buniness， 封装多个业务方法
   测试方法层级：他只调用业务层级的逻辑关系，除非业务逻辑和顺序发生变化，否则不做修改
"""



import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('tests/baidu', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')



# def suite():
#     loader = unittest.TestLoader()
#     suite = loader.discover(r'tests\login', pattern='test_*.py') # loader rests\login文件夹下test_开头的所有文件
#     return suite
#
# if __name__ == '__main__':
#     suite = suite()
#     print(suite)
#     unittest.main(defaultTest='suite')