#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def get_name():
    return 'pogoda.topr.pl'

def run_crawler():


    base_url = 'http://pogoda.topr.pl'

    response = requests.get('{}'.format(base_url))

    raw_html = response.content
    html = BeautifulSoup(raw_html, 'html.parser')

    camera_urls = []

    gallery = html.find_all('section',class_='zoom-gallery')
    for tag in gallery:
        for idx,img in enumerate(tag.find_all('img')):
            camera_name = img['alt'].encode('utf-8')
            camera_url = img['src']
            #print(camera_name, camera_url)
            camera_urls.append((camera_name, camera_url, idx))
            #print(u'camera :{}'.format(camera_name,camera_url))
    
    return camera_urls

