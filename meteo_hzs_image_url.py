#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

base_login_url="http://meteo.hzs.sk/login.php"
base_camera_url="http://meteo.hzs.sk/web_cam.php?offset=0&order_type=0&max_pictures=1&only_desc=0&time_from=&time_to=&webcam_id="
camera_id = 1

payload = {'f_user': "user", 'f_pass': "user"}
login_response = requests.post(base_login_url, data=payload)
#option_request = requests.options(base_url)

print('login_response cookies:{}'.format(login_response.cookies))

print('{}{}'.format(base_camera_url, camera_id))
response = requests.get('{}{}'.format(base_camera_url, id), 
                         cookies=login_response.cookies)

raw_html = response.content
html = BeautifulSoup(raw_html, 'html.parser')

#list all camera ids
camera_ids_list = []
for tag in html.find_all(id='webcam_id'):
	for child in tag.children:
		camera_ids_list.append(child['value'])
print(u'all places ids?:{}'.format(camera_ids_list))

#get urls for camera ids
for id in camera_ids_list:
	response = requests.get('{}{}'.format(base_camera_url, id), 
                         cookies=login_response.cookies)
	raw_html = response.content
	html = BeautifulSoup(raw_html, 'html.parser')
	#try to find place name
	for tag in html.find_all(id='webcam_id'):
		place_name = (tag.find(selected='selected').string).encode('utf-8')
		print(u'place name?:{}'.format(tag.find(selected='selected').string).encode('utf-8'))
	aTag_list = []
	for tag in html.find_all(id='picture'):
		aTag_list.append(tag['src'])
	for a in aTag_list:
		image_url = 'http://meteo.hzs.sk/{}'.format(a)
		print('http://meteo.hzs.sk/{}'.format(a))