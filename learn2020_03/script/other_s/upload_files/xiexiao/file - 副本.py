"""
@Name: file
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/7/10
"""
import os
import re
import numpy as np
import time
import operator
import oss2

# from lib.WebDriverClient import WebDriver

path_js = 'dist\static\js'
path_css = 'dist\static\css'
html_path = 'dist\index.html'

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
    # print(result + '\n')

    return result

# def files(name):
#     file = []
#     for i in name:
#         if '.js' in i:
#             i = path_js + i
#         else:
#             i = path_css + i
#         file.append(i)
#     return file

def upload_files(file):
    ''' 把更改的js、css文件上传到阿里云上 '''

    start_time = time.time()
    endpoint = 'https://oss-cn-shanghai.aliyuncs.com'
    for i in file:
        if '.js' in i:
            tmp_file = path_js + '\\' + i
            if not os.path.exists(tmp_file):
                print("File {} is not exists!".format(i))
            else:
                print("Will upload {} to the oss!".format(i))
                auth = oss2.Auth('7iFtlkzGkuWioxh5', 'cbrkUVkZSQgonvzIhrJAngpCyWwvwL')
                bucket = oss2.Bucket(auth, endpoint, 'greattone4')
                bucket.put_object_from_file('h5/static/js/' +i , tmp_file)
                print(endpoint + '/h5/static/js/'+ i)
                # print(bucket)

        else:
            tmp_file = path_css + '\\' + i
            if not os.path.exists(tmp_file):
                print("File {} is not exists!".format(i))
            else:
                print("Will upload {} to the oss!".format(i))
                auth = oss2.Auth('7iFtlkzGkuWioxh5', 'cbrkUVkZSQgonvzIhrJAngpCyWwvwL')
                bucket = oss2.Bucket(auth, endpoint, 'greattone4+')
                bucket.put_object_from_file('h5/static/css/' + i, tmp_file)
                print(endpoint + '/h5/static/css/' + i)

    print("All upload tasks have finished!")
    print("Cost {} Sec.".format(time.time() - start_time))
    # for tmp_file in file:
    #     if not os.path.exists(tmp_file):
    #         print("File {0} is not exists!".format(tmp_file))
    #     else:
    #         print("Will upload {0} to the oss!".format(tmp_file))
    #
    #         tmp_time = time.time()
    #         # cut the file name
    #         filename = tmp_file[tmp_file.rfind("/") + 1 : len(tmp_file)]
    #         ossFilename = os.path.join(FLAGS.prefix, filename)
    #         oss2.resumable_upload(
    #             bucket,
    #             ossFilename,
    #             tmp_file,
    #             progress_callback = percentage)
    #
    #         print("\nFile {0} -> {1} uploads finished, cost {2} Sec.".format(
    #             tmp_file, ossFilename, time.time() - tmp_time ))
    #
    # print("All upload tasks have finished!")
    # print("Cost {0} Sec.".format(time.time() - start_time))

# def write():
#     f = open(html_path, 'w')
#     f.write(replace())
if __name__ == '__main__':

    rep =replace()
    f = open(html_path, 'w')
    f.write(rep)
    upload_files(fileName())
    # print('替换完成')
