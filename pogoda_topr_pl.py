#-*- coding: utf-8 -*-

def get_name():
	return 'pogoda.topr.pl Camera portal'

def run_crawler():
	import requests
	from bs4 import BeautifulSoup

	base_url = 'http://pogoda.topr.pl'

	response = requests.get('{}'.format(base_url))

	raw_html = response.content
	html = BeautifulSoup(raw_html, 'html.parser')

	gallery = html.find_all('section',class_='zoom-gallery')
	for tag in gallery:
		for img in tag.find_all('img'):
			print(u'name:{}'.format((img['alt']).encode('utf-8')))	
			print(u'camera :{}'.format(img['src']))

	for url in html.find_all('img',alt='Morskie Oko'):
		if url.parent.name == 'a':
			print('response={}'.format(url.get('src')))

