
"""
@Name: test
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/10/15
"""
import oss2
# from appium import webdriver
# import time
# import os
#
# #初始化信息
#
# PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
#
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '7.0'
# desired_caps['deviceName'] = 'Android Emulator'
# desired_caps['appPackage'] = 'com.greattone.greattone'
# desired_caps['appActivity'] = 'com.greattone.greattone.activity.StartActivity'
# desired_caps["app"] = PATH("F:\\python\\pythonLearn\\test\\AndriodGreat\\packages\\apps-release.apk")
#
# print(type(desired_caps))
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
# time.sleep(10)


# def oss(img_key, img_path):
#
#     auth = oss2.Auth('LTA。。。。。。', '3XkJh。。。。。。')
#     endpoint = 'http://oss-cn-qingdao.aliyuncs.com'
#     bucket = oss2.Bucket(auth, endpoint, 'dasheng1104')
#     bucket.put_object_from_file(img_key, img_path)
#
# if __name__=="__main__":
#     img_key = str(uuid.uuid4()) + '.jpg'
#     img_path = '/Users/kunlun/Downloads/purchase_process_1.png'
#     oss(img_key, img_path)
#     print "upload success!"
