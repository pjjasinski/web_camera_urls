from django.core.management.base import BaseCommand, CommandError
from weburls.models import Portal as Portal
import os

class Command(BaseCommand):
    help = 'Creates portal from cam_crawler/ directory scripts'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        list_dir = os.listdir('./cam_crawler')
        for portal_script in list_dir:
            if '.py' in portal_script:
                f = open('./cam_crawler/' + portal_script).read()
                if 'def run_crawler():' in f:
                    script_name = portal_script.split('.')[0]
                    portals = Portal.objects.filter(title=script_name)
                    if len(portals) == 0:
                        portal = Portal.objects.create_portal(script_name)
                        portal.save()
                        self.stdout.write(self.style.SUCCESS('Found script, create portal:"%s"' % script_name))