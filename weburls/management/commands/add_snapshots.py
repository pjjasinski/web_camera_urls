from django.core.management.base import BaseCommand, CommandError
from weburls.models import Snapshot as Snapshot
from weburls.models import Camera as Camera
from weburls.models import Portal as Portal
import importlib

class Command(BaseCommand):
    help = 'Adds the Snapshot'

    def add_arguments(self, parser):
        parser.add_argument('portal', nargs='+', type=str)

    def handle(self, *args, **options):
        portal_title=(options['portal'])[0]

        portals = Portal.objects.filter(title=portal_title)

        if len(portals) == 0:
            raise CommandError('Portal "%s" does not exist' % portal_title)
        try:
            portal_package = 'cam_crawler.' + portal_title
            self.stdout.write(str(portal_package))
            lib = importlib.import_module(portal_package)
        except:
            raise CommandError('Portal package "%s" does not exist' % portal_title)

        urls = lib.run_crawler()

        for url in urls:
            camera_url = url[1]
            camera_title = url[0]
            on_portal_id = url[2]

            cameras = Camera.objects.filter(on_portal_id=on_portal_id, title=camera_title)

            if len(cameras) == 0:
                camera = Camera.objects.create_camera(camera_title, portal_title, on_portal_id)
                camera.save()
            else:
                camera = cameras[0]

            snap = Snapshot.objects.filter(url=camera_url, camera=camera)
            if len(snap):
                self.stdout.write(self.style.SUCCESS('Already in database'))
            else:    
                snap = Snapshot.objects.create_snapshot(camera_url, camera.pk)
                snap.save()

        self.stdout.write(self.style.SUCCESS('Successfully added snapshots for "%s"' % portal_title))
