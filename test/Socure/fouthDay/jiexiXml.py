"""
@Name: KuhuCode
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/1/25
"""

import os
import xml.etree.ElementTree as ET
import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

data = open('E:/桌面/note.xml').read()
tree = ET.parse("country.xml")
root = ET.fromstring(data)
# print(tree)
print(root)
