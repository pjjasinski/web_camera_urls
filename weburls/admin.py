from django.contrib import admin

from .models import Portal
from .models import Camera
from .models import Snapshot

admin.site.register(Portal)
admin.site.register(Camera)
admin.site.register(Snapshot)
