"""
@Name: address
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/8/28
"""
'''
替换数据库中的图片url，将本地路径替换为阿里云路径

'''

import os
import shutil
import pymysql
import urllib
import re
import time
import numpy as np
import string

config = {
    'host': 'rm-uf6e3o17651w13pq28o.mysql.rds.aliyuncs.com',
    'port': 3306,
    'user': 'zjk',
    'password': 'zjk940915++',
    'db': 'hao',
    'charset': 'utf8'
}
# path = 'news.txt'
# config = {
#     'host': '47.100.60.152',
#     'port': 3306,
#     'user': 'gttest',
#     'password': 'COk+Y5.g8FDxJ5s',
#     'db': 'ceshihao3.6',
#     'charset': 'utf8'
# }

conn = pymysql.connect(**config)
cur = conn.cursor()

# def photo(dirname):
# 	subdir_list = []
# 	for maindir, subdir, file_name_list in os.walk(dirname):
# 		# print('1:',maindir)
# 		# print('2:',subdir)
# 		# print('3:', file_name_list)
#
# 		# path = os.path.abspath(dirname)
# 		if len(file_name_list) != 1:
# 			for item in subdir:
# 				# print(item)
# 				newname = item + '_big.jpg'
# 				aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/head_pic/' + item + '_big.jpg'
# 				# cur.execute("UPDATE gt004_user_teacher set tc004_user_pic = '%s' where tc004_user_pic like '%%/d/photo/%%' and tc004_user_pic like '%%%s%%' ORDER BY tc004_num_follow desc"%(aliyun_href,item))
# 				# conn.commit()
# 				# cur.execute("UPDATE gt005_user_store set tc005_user_pic = '%s' where tc005_user_pic like '%%/d/photo/%%' and tc005_user_pic like '%%%s%%' ORDER BY tc005_num_follow desc"%(aliyun_href,item))
# 				# conn.commit()
#
# 				cur.execute("SELECT tc004_user_pic, tc001_user_id from gt004_user_teacher where tc004_user_pic like '%%/d/photo/%%'")
# 				user = cur.fetchall()
#				# print(user)
#  				i = 0
# 				for user_item in user:
# 					select_pic = re.findall(r"\d+\.?\d*", user_item[0])
# 					i += 1
# 					print(select_pic[0],item, i)
# 					print('='*50)
# 					if select_pic[0] == item:
# 						print(select_pic)
# 						cur.execute("UPDATE gt004_user_teacher set tc004_user_pic = '%s' where tc001_user_id = '%s'"%(aliyun_href,user_item[1]))
# 						conn.commit()
# 					print('='*100)
#
# 				cur.execute("SELECT tc005_user_pic, tc001_user_id from gt005_user_store where tc005_user_pic like '%%/d/photo/%%'")
# 				user = cur.fetchall()
# 				for user_item in user:
# 					select_pic = re.findall(r"\d+\.?\d*", user_item[0])
# 					i += 1
# 					print(select_pic[0], item, i)
# 					print('=' * 50)
# 					if select_pic[0] == item:
# 						print(select_pic)
# 						cur.execute("UPDATE gt005_user_store set tc005_user_pic = '%s' where tc001_user_id = '%s'" % (aliyun_href, user_item[1]))
# 						conn.commit()
#
# 				# cur.execute("SELECT tc005_user_pic, tc001_user_id from gt005_user_store where tc005_user_pic like '%%%s%%' and tc005_user_pic like '%%/d/photo/%%'" % item)
# 				# user = cur.fetchone()
# 				# if re.findall(r"\d+\.?\d*", user[0]) == item:
# 				# 	cur.execute("UPDATE gt004_user_teacher set tc004_user_pic = '%s' where tc001_user_id = '%s'" % (
# 				# 	item, user[1]))
# 				# 	conn.commit()
#
# 				# subdir_list.append(aliyun_href)
# 				# os.chdir(path+'\\'+item)
# 				# if os.path.exists('big.jpg'):
# 				# 	shutil.copyfile('big.jpg', newname)
# 				# 	shutil.move(newname, path+'\\' +'new')
# 	# print(subdir_list)
#
# def all_path(dirname):
# 	for maindir, subdir, file_name_list in os.walk(dirname):
# 		if len(file_name_list) != 1:
# 			for item in subdir:
# 				# print(item)
# 				aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/head_pic/' + item + '_big.jpg'
# 				old_pic = '/d/photo/' + item + '/big.jpg'
# 				cur.execute("UPDATE phome_enewsmemberadd set userpic = '%s' where userpic = '%s'" % (aliyun_href,old_pic))
# 				conn.commit()
# 				print(aliyun_href)
# 				# cur.execute("SELECT userpic,userid from phome_enewsmemberadd where userpic = '%s'"%old_pic)
# 				# user = cur.fetchall()
# 				# i = 0
# 				# for user_item in user:
# 				# 	select_pic = re.findall(r"\d+\.?\d*", user_item[0])
# 				# 	i += 1
# 				# 	print(select_pic[0],item, i)
# 				# 	print('='*50)
# 				# 	if select_pic[0] == item:
# 				# 		print(select_pic)
# 				# 		cur.execute("UPDATE phome_enewsmemberadd set userpic = '%s' where userid = '%s'"%(aliyun_href,user_item[1]))
# 				# 		conn.commit()
# 				# 	print('='*100)
#
# def upload(dirname):
# 	for maindir, subdir, file_name_list in os.walk(dirname):
# 		path = os.path.abspath(dirname)
# 		print(file_name_list)
# 		i = 0
# 		for item in file_name_list:
# 			old_pic = '/shang/upload/' + item
# 			aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/head_pic/' + item
# 			cur.execute("select userpic,userid from phome_enewsmemberadd where userpic = '%s'" % old_pic)
# 			user = cur.fetchall()
# 			print(user, i)
# 			i += 1
# 			if len(user) != 0:
# 				for user_item in user:
# 					# cur.execute("UPDATE phome_enewsmemberadd set userpic = '%s' where userid = '%s'" % (aliyun_href, user_item[1]))
# 					# conn.commit()
# 					os.chdir(path)
# 					shutil.move(item, path+'\\' +'exss')
# 					print(user_item,aliyun_href)
#
# def userpic(dirname):
# 	for maindir, subdir, file_name_list in os.walk(dirname):
# 		path = os.path.abspath(dirname)
# 		print(file_name_list)
# 		i = 0
# 		for item in file_name_list:
# 			old_pic = 'http://zjk.franzsandner.com/d/uploaduserpic/userpic/' + item
# 			aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/head_pic/' + item
# 			cur.execute(
# 				"select userpic,userid from phome_enewsmemberadd where  userpic like '%%http://zjk.franzsandner.com/d/uploaduserpic/userpic%%' and userpic = '%s'" % old_pic)
# 			user = cur.fetchall()
# 			print(user, i)
# 			i += 1
# 			if len(user) != 0:
# 				for user_item in user:
# 					# cur.execute("UPDATE phome_enewsmemberadd set userpic = '%s' where userid = '%s'" % (aliyun_href, user_item[1]))
# 					# conn.commit()
# 					os.chdir(path)
# 					shutil.move(item, path + '\\' + 'exss')
# 					print(user_item, aliyun_href)
# 					# file_name_list.remove(item)
#
# 		i = 0
# 		for item in file_name_list:
# 			old_pic = 'http://www.sheyingnet.net/d/uploaduserpic/userpic/' + item
# 			aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/head_pic/' + item
# 			cur.execute(
# 				"select userpic,userid from phome_enewsmemberadd where userpic like '%%http://www.sheyingnet.net/d/uploaduserpic/userpic/%%' and userpic = '%s'" % old_pic)
# 			user = cur.fetchall()
# 			print(user, i)
# 			i += 1
# 			if len(user) != 0:
# 				for user_item in user:
# 					# cur.execute("UPDATE phome_enewsmemberadd set userpic = '%s' where userid = '%s'" % (aliyun_href, user_item[1]))
# 					# conn.commit()
# 					os.chdir(path)
# 					shutil.move(item, path + '\\' + 'exss')
# 					print(user_item, aliyun_href)
# 					# file_name_list.remove(item)
#
# 		i = 0
# 		for item in file_name_list:
# 			old_pic = 'http://www.greattone.net/d/uploaduserpic/userpic/' + item
# 			aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/head_pic/' + item
# 			cur.execute(
# 				"select userpic,userid from phome_enewsmemberadd where userpic like '%%http://www.greattone.net/d/uploaduserpic/userpic/%%' and userpic = '%s'" % old_pic)
# 			user = cur.fetchall()
# 			print(user, i)
# 			i += 1
# 			if len(user) != 0:
# 				for user_item in user:
# 					# cur.execute("UPDATE phome_enewsmemberadd set userpic = '%s' where userid = '%s'" % (aliyun_href, user_item[1]))
# 					# conn.commit()
# 					os.chdir(path)
# 					shutil.move(item, path + '\\' + 'exss')
# 					print(user_item, aliyun_href)
#
# 		i = 0
# 		for item in file_name_list:
# 			old_pic = 'http://greattone.net/d/uploaduserpic/userpic/' + item
# 			aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/head_pic/' + item
# 			cur.execute(
# 				"select userpic,userid from phome_enewsmemberadd where userpic like '%%http://greattone.net/d/uploaduserpic/userpic/%%' and userpic = '%s'" % old_pic)
# 			user = cur.fetchall()
# 			print(user, i)
# 			i += 1
# 			if len(user) != 0:
# 				for user_item in user:
# 					# cur.execute("UPDATE phome_enewsmemberadd set userpic = '%s' where userid = '%s'" % (aliyun_href, user_item[1]))
# 					# conn.commit()
# 					os.chdir(path)
# 					shutil.move(item, path + '\\' + 'exss')
# 					print(user_item, aliyun_href)
#


# path = 'F:\\python\\PythonLearn\\test\\MysqlData\\image'
# new_path = 'F:\\python\\PythonLearn\\test\\MysqlData\\image\\oss'
#
# for root, dirs, files in os.walk(path):
# 	if len(dirs) == 0:
# 		# print(dirs)
# 		# print(files)
# 		for i in range(len(files)):
# 			# print(files[i])
# 			# if files[i][-3:-1] == 'png' or files[i][]:
# 			file_path = root + '/' + files[i]
# 			new_file_path = new_path + '/' + files[i]
# 			shutil.move(file_path, new_file_path)


# def download_picture(url):
# 	file_name = url.split('/')[-1]
# 	r = urllib.request.urlopen(url,headers)
# 	data = r.read()
# 	with open(file_name, 'wb') as f:
# 		f.write(data)

# def down(url):
# 	try:
# 		# headers= 'User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Firefox/51.0'
# 		if not os.path.exists(root):
# 			os.mkdir(root)
# 		if not os.path.exists(path):
# 			print(1)
# 			print(url)
#
# 			r = requests.get(url)
# 			print(r)
# 			r.raise_for_status()
# 			#使用with语句可以不用自己手动关闭已经打开的文件流
# 			with open(path,"wb") as f: #开始写文件，wb代表写二进制文件
# 				f.write(r.content)
# 			print("爬取完成")
# 		else:
# 			print("文件已存在")
# 	except Exception as e:
# 		print("爬取失败:"+str(e))
# #
# if __name__ == '__main__':
# 	root = "F://python//picture//"
# #
# # 	download_picture('http://old.greattone.com.com/d/uploaduserpic/userpic/1464758336.jpg')
#
# 	cur.execute("SELECT tc069_url FROM gt069_user_photo where tc069_url not like '%greattone.oss-cn-shanghai.aliyuncs.com%' and tc069_url !=''")
# 	user = cur.fetchall()
#
# 	for item in user:
# 		image_url = item[0]
# 		# print(item)
# 		# if len(item) == 1:
# 		if  'm.greattone' in image_url:
# 			new_url = image_url.replace('m.greattone', 'old.greattone')
# 			path = root + image_url.split("/")[-1]
# 			down(new_url )
# 			print('m.greattone')
# 		elif '/d/images/wanshanziliao/jiaoshi/uploads/' in image_url:
# 			new_url = 'http://old.greattone.net' + image_url
# 			path = root + image_url.split("/")[-1]
# 			down(new_url)

#
#
#
#
#
#
# # cur.execute("SELECT tc060_url_pic,tc060_lesson_id FROM gt060_lesson where tc060_url_pic like '%%/ueditor/php/upload/image/%%';")
# # user = cur.fetchall()
# #
# #
# #
# def image():
#
# 	# list_pic = []
# 	cur.execute("SELECT tc060_url_pic,tc060_lesson_id FROM gt060_lesson WHERE tc060_url_pic not like '%%greattone.oss-cn-shanghai.aliyuncs.com%%' and tc060_url_pic != ''")
# 	user = cur.fetchall()
#
# 	for item in user:
# 		print(item)
#
# 		name_pic = item[0].split('/')[-1]
# 		aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/images/cover/lesson/'+ name_pic
# 		cur.execute("UPDATE gt060_lesson set tc060_url_pic = '%s' where tc060_lesson_id='%s'"%(aliyun_href,item[1]))
# 		conn.commit()
# 		print(aliyun_href)
#
# def image1():
#
# 	# list_pic = []
# 	cur.execute("SELECT tc054_url_pic,tc054_piano_room_id FROM gt054_piano_room WHERE tc054_url_pic not like '%%greattone.oss-cn-shanghai.aliyuncs.com%%' and tc054_url_pic != ''")
# 	user = cur.fetchall()
#
# 	for item in user:
# 		print(item)
#
# 		name_pic = item[0].split('/')[-1]
# 		aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/images/cover/room/' + name_pic
# 		cur.execute(
# 			"UPDATE gt054_piano_room set tc054_url_pic = '%s' where tc054_piano_room_id='%s'" % (aliyun_href, item[1]))
# 		conn.commit()
# 		print(aliyun_href)
#
# def image2():
#
# 	# list_pic = []
# 	cur.execute("SELECT tc069_url,tc069_user_photo_id FROM gt069_user_photo where tc069_url not like '%greattone.oss-cn-shanghai.aliyuncs.com%' and tc069_url !=''")
# 	user = cur.fetchall()
#
# 	for item in user:
# 		print(item)
#
# 		name_pic = item[0].split('/')[-1]
# 		aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/images/user_photo/' + name_pic
# 		cur.execute(
# 			"UPDATE gt069_user_photo set tc069_url = '%s' where tc069_user_photo_id='%s'" % (
# 				aliyun_href, item[1]))
# 		conn.commit()
# 		print(aliyun_href)

# def image3():
#
# 	# list_pic = []
# 	cur.execute(
# 		"SELECT tc028_pic_url, tc028_id FROM gt028_activity where tc028_pic_url like '%/d/file/%' and tc028_pic_url !=''")
# 	user = cur.fetchall()
# 	print(user)
#
# 	for item in user:
# 		print(item)
#
# 		name_pic = item[0].split('/')[-1]
# 		aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/images/cover/actvity/' + name_pic
# 		cur.execute(
# 			"UPDATE gt028_activity set tc028_pic_url = '%s' where tc028_id='%s'" % (
# 				aliyun_href, item[1]))
# 		conn.commit()
# 		print(aliyun_href)

# def image4():
#
# 	# list_pic = []
# 	cur.execute(
# 		"SELECT tc028_pic_url, tc028_id FROM gt028_activity where tc028_pic_url like '%www.greattone.net%' and tc028_pic_url !=''")
# 	user = cur.fetchall()
# 	print(user)
#
# 	for item in user:
# 		print(item)
#
# 		name_pic = item[0].split('/')[-1]
# 		aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/images/cover/actvity/' + name_pic
# 		cur.execute(
# 			"UPDATE gt028_activity set tc028_pic_url = '%s' where tc028_id='%s'" % (
# 				aliyun_href, item[1]))
# 		conn.commit()
# 		print(aliyun_href)

# def image5():
#
# 	cur.execute(
# 		"SELECT tc093_cover_plan_url,tc093_id  FROM gt093_dynamic_long")
# 	user = cur.fetchall()
#
# 	for item in user:
#
# 		name_pic = item[0].split('/')[-1]
# 		aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/article/cover_pic/' + name_pic
# 		cur.execute(
# 			"UPDATE gt093_dynamic_long set tc093_cover_plan_url = '%s' where tc093_id='%s'" % (
# 				aliyun_href, item[1]))
# 		conn.commit()
# 		print(aliyun_href)

# def image6():
#
# 	cur.execute("SELECT tc028_introduce,tc028_id  FROM gt028_activity ")
# 	# cur.execute("SELECT newstext  FROM phome_ecms_news_data_1,phome_ecms_news where phome_ecms_news.id=phome_ecms_news_data_1.id and titlepic !='' and truetime>1514736000 ")
# 	user = cur.fetchall()
#
# 	# for item in user:
# 	# 	pattern = re.compile(r'http://www(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
# 	# 	urls = re.findall(pattern, item[0])
# 	# 	for url in urls:
# 	# 		url=url[:-1]
# 	# 		if url.endswith('g', len(url)-1,len(url))==True or url.endswith('f', len(url)-1,len(url))==True:
# 	# 			with open(path, 'a') as f:
# 	# 				f.write(url + '\n')
# 	# 				print(url)
#
# 	# for item in user:
# 	# 	pattern = re.compile(r'/ueditor.*?.\"')
# 	# 	urls = re.findall(pattern, item[0])
# 		# print(urls,item[1])
# 		# for url in urls:
# 		# 	url = url[:-2]
# 		# 	print(url)
# 	# 		if 'jpeg' in url:
# 	# 			# print(url)
# 	# 			url = url[:-2]
# 	# 			name_pic = url.split('/')[-1]
# 	# 			aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/article/content/' + name_pic
# 	# 			cur.execute(
# 	# 				"UPDATE gt093_dynamic_long set tc093_long_text = REPLACE(tc093_long_text,'%s','%s') where tc093_id='%s'" % (url,aliyun_href, item[1]))
# 	# 			conn.commit()
# 	# 			print(aliyun_href)
# 	# 		else:
# 	# 			url=url[:-1]
# 	# 			name_pic = url.split('/')[-1]
# 	# 			aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/article/content/' + name_pic
# 	# 			cur.execute(
# 	# 				"UPDATE gt093_dynamic_long set tc093_long_text = REPLACE(tc093_long_text,'%s','%s') where tc093_id='%s'" % (url,aliyun_href, item[1]))
# 	# 			conn.commit()
# 	# 			print(aliyun_href)
#
# 	i = 0
#
# 	for item in user:
# 		pattern = re.compile(r'https://www.greattone.net/ueditor/php/upload/image/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
# 		urls = re.findall(pattern, item[0])
# 		# print(urls)
# 		for url in urls:
# 			url=url[:-1]
# 			print(url)
# 			# if url.endswith('g', len(url)-1,len(url))==True or url.endswith('f', len(url)-1,len(url))==True:
# 			name_pic = url.split('/')[-1]
# 			aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/activity/content/' + name_pic
# 			cur.execute(
# 				"UPDATE gt028_activity set tc028_introduce = REPLACE(tc028_introduce,'%s','%s') where tc028_id='%s'" % (url,aliyun_href, item[1]))
# 			conn.commit()
# 			print(aliyun_href)


# def activity028():
#
# 	cur.execute("SELECT tc028_introduce,tc028_id FROM gt028_activity")
# 	user = cur.fetchall()
# 	# print(user)
# 	# for items in user:
# 	# 	pattern = re.compile(r'https://www.greattone.net/ueditor.*?.\\') # /ueditor/php/upload/image/20180727/1532675917750782.jpg\\
# 	# 	pic_names = re.findall(pattern, items[0])
# 	# 	print(pic_names)
# 	# 	for image in pic_names:
# 	# 		name = image[:-1].split('/')[-1] # 图片名称
# 	# 		print(name,items[-1])
# 	# 		aliyun_href = 'http://greattone4.oss-cn-shanghai.aliyuncs.com/activity/content/' + name # 阿里云图片地址
# 	# 		cur.execute("UPDATE gt028_activity set tc028_introduce = REPLACE(tc028_introduce, '%s', '%s') where tc028_id='%s'" % (
# 	# 				image[:-1], aliyun_href, items[1]))
# 	# 		conn.commit()
# 	# 		print(items[1],aliyun_href)
#
# 	for items in user:
# 		pattern = re.compile(
# 			r'/ueditor.*?.\\')  # /ueditor/php/upload/image/20180727/1532675917750782.jpg\\
# 		pic_names = re.findall(pattern, items[0])
# 		print(pic_names)
# 		for image in pic_names:
# 			name = image[:-1].split('/')[-1]  # 图片名称
# 			aliyun_href = 'http://greattone4.oss-cn-shanghai.aliyuncs.com/activity/content/' + name  # 阿里云图片地址
#
# 			cur.execute(
# 				"UPDATE gt028_activity set tc028_introduce = REPLACE(tc028_introduce, '%s', '%s') where tc028_id='%s'" % (
# 					image[:-1], aliyun_href, items[1]))
# 			conn.commit()
			# print(aliyun_href)


# def dynamic_94():
# 	cur.execute("SELECT tc094_url_photo,tc094_id FROM gt094_dynamic_apply")
# 	user = cur.fetchall()
# 	# print(user)
# 	for items in user:
# 		# print(items)
# 		pattern = re.compile(r'https://(?:m|www).greattone.net/d.*(?:jpg|png|bmp)')
# 		pic_names = re.findall(pattern, items[0])
# 		if len(pic_names)>=1:
# 			name = pic_names[0].split('/')[-1] # 图片名称
# 			aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/images/cover/' + name # 阿里云图片地址
# 			cur.execute("UPDATE gt094_dynamic_apply set tc094_url_photo = '%s' where tc094_id='%s'" % (
# 					aliyun_href, items[1]))
# 			conn.commit()
# 			print(pic_names)

def userpic_94():

	cur.execute("SELECT tc094_user_id,tc094_id FROM gt094_dynamic_apply WHERE tc028_act_id='305'")
	user = cur.fetchall()
	# print(user)
	users=''
	i = 0
	for items in user:
		users = users + "'" + items[0] + "'" + ','
		i = i+1
	print(i)
	print(users)
		# 	name = pic_names[0].split('/')[-1]  # 图片名称
		# 	aliyun_href = 'https://greattone4.oss-cn-shanghai.aliyuncs.com/images/cover/' + name  # 阿里云图片地址
		# 	cur.execute("UPDATE gt094_dynamic_apply set tc094_url_photo = '%s' where tc094_id='%s'" % (
		# 		aliyun_href, items[1]))
		# 	conn.commit()
		# 	print(pic_names)


# all_path('photo')
# upload('upload')
# userpic('userpic')
# image('image')
# image()
# image1()
# image2()
# image4()
# image5()
# activity028()
# dynamic_94()
userpic_94()