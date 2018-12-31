from django.db import models

class Portal(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')

	def __str__(self):
		return "%s" % self.title

class CameraManager(models.Manager):
	def create_camera(self, title, portal_title, on_portal_id):
		portal = Portal.objects.get(title=portal_title)
		camera = self.create(title=title,on_portal_id=on_portal_id,portal=portal)
		return camera

class Camera(models.Model):
	portal = models.ForeignKey(Portal, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	on_portal_id = models.CharField(max_length=100, blank=True, default='')

	objects = CameraManager()

	def __str__(self):
		return "%s" % self.title

class SnapshotManager(models.Manager):
	def create_snapshot(self, url, camera_id):
		camera = Camera.objects.get(pk=camera_id)
		snapshot = self.create(url=url,camera=camera)
		return snapshot

class Snapshot(models.Model):
	camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	url = models.CharField(max_length=500, blank=False, default='')

	objects = SnapshotManager()

	def __str__(self):
		return "%s -- %s" % (self.created, self.url)

	class Meta:
		ordering = ('created',)
	