"""
@Name: file
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/7/10
"""
import os
import re
# import numpy as np
# from lib.WebDriverClient import WebDriver

path_js = 'dist\static\js'
path_css = 'dist\static\css'
html_path = 'dist\index.html'
png = 'D://program data//weixin//WeChat Files//zimengrao//FileStorage//File//2019-11'

'''
H5项目 .js路径替换成阿里云路径
项目使用阿里云上的.js的话，就需要将此脚本运行下，并把下面的文件上传到阿里云上
'''

def oneName(path):

    for root, dirs, files in os.walk(path):
        return files

def fileName():
    Name = np.append(oneName(path_css), oneName(path_js)).tolist()

    name = [item for item in Name if '.map' not in item and len(item) > 25]
    print(name)
    return name


def replace():
    app_css, app_js, manifest_js, vendor_js = fileName()
    app_css = 'href=https://greattone4.oss-cn-shanghai.aliyuncs.com/h5/static/css/' + app_css
    app_js = 'src=https://greattone4.oss-cn-shanghai.aliyuncs.com/h5/static/js/' + app_js
    manifest_js = 'src=https://greattone4.oss-cn-shanghai.aliyuncs.com/h5/static/js/' + manifest_js
    vendor_js = 'src=https://greattone4.oss-cn-shanghai.aliyuncs.com/h5/static/js/' + vendor_js
    content = open(html_path, 'r').read()
    pattern = re.compile(r'href=./static/css/app.(.*?).css')
    result = pattern.sub(app_css, content)

    pattern = re.compile(r'src=./static/js/app.(.*?).js')
    result = pattern.sub(app_js, result)

    pattern = re.compile(r'src=./static/js/manifest.(.*?).js')
    result = pattern.sub(manifest_js, result)

    pattern = re.compile(r'src=./static/js/vendor.(.*?).js')
    result = pattern.sub(vendor_js, result)
    print(result + '\n')

    return result

def gif_to_png(png):

    file_names = os.listdir(png)
    # print(file_names)

    for item in file_names:
        print(item)
        if '.gif' in item:
            # position = name.rfind(item)
            new_name = item.replace('.gif', '.png')
            # os.rename(png + '/' + item, png + '/' + new_name)
            # print(item)
        # print(item)


# def write():
#     f = open(html_path, 'w')
#     f.write(replace())
if __name__ == '__main__':

    # rep =replace()
    # f = open(html_path, 'w')
    # f.write(rep)

    gif_to_png(png)