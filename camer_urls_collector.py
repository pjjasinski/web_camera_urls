#-*- coding: utf-8 -*-
import meteo_hzs_image_url
import pogoda_topr_pl

class CameraPortal(object):
	def __init__(self, module):
		super(CameraPortal, self).__init__()
		self.function_to_run = module.run_crawler
		self.portal_name = module.get_name()

	def run(self):
		self.function_to_run()
	
	def get_name(self):
		return self.portal_name

class Camera_Urls_Collector(object):
	def __init__(self):
		self.portal_list = []
		pass

	def register_portal(self, portal):
		self.portal_list.append(portal)

	def run_collector(self):
		for portal in self.portal_list:
			print('Runnning:{}'.format(portal.get_name()))
			portal.run()



if __name__ == '__main__':
	print('Test collector')

	meteo_portal = CameraPortal(meteo_hzs_image_url)
	topr_portal = CameraPortal(pogoda_topr_pl)

	collector = Camera_Urls_Collector()
	#collector.register_portal(meteo_portal)
	collector.register_portal(topr_portal)
	collector.run_collector()


