#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def get_name():
    return 'meteo.hzs.sk'

def run_crawler():
    base_login_url="http://meteo.hzs.sk/login.php"
    base_camera_url="http://meteo.hzs.sk/web_cam.php?offset=0&order_type=0&max_pictures=1&only_desc=0&time_from=&time_to=&webcam_id="

    payload = {'f_user': "user", 'f_pass': "user"}
    login_response = requests.post(base_login_url, data=payload)

    response = requests.get('{}{}'.format(base_camera_url, 1), 
                             cookies=login_response.cookies)

    raw_html = response.content
    html = BeautifulSoup(raw_html, 'html.parser')

    #list all camera ids
    camera_ids_list = []
    for tag in html.find_all(id='webcam_id'):
        for child in tag.children:
            camera_ids_list.append(child['value'])

    #get urls for camera ids
    camera_urls = []

    for idx in camera_ids_list:
        response = requests.get('{}{}'.format(base_camera_url, idx), 
                             cookies=login_response.cookies)
        raw_html = response.content
        html = BeautifulSoup(raw_html, 'html.parser')
        #try to find place name
        for tag in html.find_all(id='webcam_id'):
            place_name = (tag.find(selected='selected').string).encode('windows-1250')
        aTag_list = []
        for tag in html.find_all(id='picture'):
            aTag_list.append(tag['src'])
        for a in aTag_list:
            image_url = 'http://meteo.hzs.sk/{}'.format(a)
            camera_urls.append((place_name, image_url, idx))
            print('name:{}'.format(place_name))
    return camera_urls
