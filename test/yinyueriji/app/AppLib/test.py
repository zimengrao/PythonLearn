
"""
@Name: test
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/10/15
"""

from appium import webdriver
import time
import os

#初始化信息

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.greattone.greattone'
desired_caps['appActivity'] = 'com.greattone.greattone.activity.StartActivity'
desired_caps["app"] = PATH("F:\\python\\pythonLearn\\test\\AndriodGreat\\Apps\\app-release.apk")

print(type(desired_caps))
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
time.sleep(10)
