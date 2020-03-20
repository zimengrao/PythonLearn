"""
@Name: devices
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2019/4/15
"""
import os

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
class Devices:
    Devices = {
        "phone1": [
            {
                'platformName': 'Android',
                'platformVersion': '8.0.0',
                'deviceName': 'MKJNW18928001740',
                'apppackage': 'com.greattone.greattone',
                'appactivity': 'com.greattone.greattone.activity.StartActivity',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'autoGrantPermissions': True,
                'automationName': 'uiautomator2',
                'app': PATH("packages/apps-release.apk")
            },
            {
                'driver_url': 'http://localhost:4723/wd/hub'
            }
        ]
    }