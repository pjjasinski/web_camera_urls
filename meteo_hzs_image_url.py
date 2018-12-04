import requests
from bs4 import BeautifulSoup

base_url="http://meteo.hzs.sk/login.php"

payload = {'f_user': "user", 'f_pass': "user"}
response = requests.post(base_url, data=payload)
option_request = requests.options(base_url)

print('options response:{}'.format(option_request.headers))
 
response2 = requests.get("http://meteo.hzs.sk/web_cam.php?offset=0&order_type=0&max_pictures=100"
                         "&only_desc=0&time_from=&time_to=&webcam_id=12", cookies=response.cookies)

raw_html = response2.content
html = BeautifulSoup(raw_html, 'html.parser')

link_list = []

for link in html.find_all(id='picture'):
	link_list.append(link['src'])
	print('html = {}'.format(link['src']))

for link in link_list:
	print('http://meteo.hzs.sk/{}'.format(link))