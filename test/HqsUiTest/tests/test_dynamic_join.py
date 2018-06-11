"""
@Name: test_fatie
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/5
"""
# import lib
# import unittest
# import time
# from config import Config
# import select,socket
#
# class HqsTestCases(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#
#         cls.config = Config.enum.get('hqs')
#         cls.dynamic = cls.config.get('dynamic')
#         cls.value = cls.dynamic.get('value')
#         cls.click_video, cls.click_music, cls.click_photo = cls.dynamic.get('click_dynamic')
#
#         cls.video_title, cls.video_content, cls.video_xpath, cls.video_send= cls.dynamic.get('video').get('video')
#         cls.video_file = cls.dynamic.get('video').get('video_file')
#
#         cls.music_title, cls.music_content, cls.music_select, cls.music_upload, cls.music_send = cls.dynamic.get('music').get('music')
#         cls.music_file = cls.dynamic.get('music').get('music_file')
#
#         cls.photo_title, cls.photo_content, cls.photo_select, cls.photo_select1, cls.photo_select2, cls.photo_upload, cls.photo_send = cls.dynamic.get('photo').get('photo')
#         cls.photo_file = cls.dynamic.get('photo').get('photo_file')
#
#         cls.assert_url, cls.assert_login, cls.assert_dynamic = cls.config.get('assert_xpath')
#
#     def setUp(self):
#         self.lib = lib.BusinessApi(self.config)
#         self.driver = self.lib.driver
#
#     def tearDown(self):
#         self.driver.quit()
#
#     # def test_video_is_ok(self):
#     #     '''发布视频动态 is ok'''
#     #     self.lib.hqs_guangchang()
#     #     self.lib.send_keys(self.video_title, self.value)
#     #     self.lib.send_keys(self.video_content, self.value)
#     #     self.lib.send_keys(self.video_xpath,self.video_file)
#     #     self.lib.click(self.video_send)
#     #     time.sleep(10)  # 上传视频时间，上传小于3min的视频
#     #
#     #     self.assertEqual('测试内容', self.lib.parse(self.assert_dynamic)[0])
#
#     def test_music_is_ok(self):
#         '''发布音乐动态 is ok'''
#         self.lib.hqs_guangchang()
#         self.lib.click(self.click_music)
#         time.sleep(1)
#         self.lib.send_keys(self.music_title, self.value)
#         self.lib.send_keys(self.music_content, self.value)
#         self.lib.click(self.music_select)
#         print(self.music_file)
#         self.lib.hqs_uploads(self.music_file)
#         time.sleep(5)
#         self.lib.click(self.music_upload)
#         time.sleep(2)
#         self.lib.click(self.music_send)
#         time.sleep(3)
#         self.assertEqual('测试内容', self.lib.parse(self.assert_dynamic)[0])
#
#     # def test_photo_is_ok(self):
#     #     '''发布音乐动态 is ok'''
#     #     self.lib.hqs_guangchang()
#     #     self.lib.click(self.click_photo)
#     #     time.sleep(1)
#     #     self.lib.send_keys(self.photo_title, self.value)
#     #     self.lib.send_keys(self.photo_content, self.value)
#     #     self.lib.click(self.photo_select)
#     #     time.sleep(0.5)
#     #     all_pic = self.photo_file
#     #     i = 0
#     #     for pic in all_pic:
#     #         if i == 0:
#     #             self.lib.click(self.photo_select1)
#     #             os.system("upload.exe %s" % pic)
#     #             time.sleep(3)
#     #         else:
#     #             self.lib.click(self.photo_select2)
#     #             os.system("upload.exe %s" % pic)
#     #             time.sleep(3)
#     #         i += 1
#     #     self.lib.click(self.photo_upload)
#     #     time.sleep(2)
#     #     self.lib.click(self.photo_send)
#     #     time.sleep(3)
#     #     self.assertEqual('测试内容', self.lib.parse(self.assert_dynamic)[0])


