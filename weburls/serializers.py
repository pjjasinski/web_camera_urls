from rest_framework import serializers
from weburls.models import Snapshot, Camera, Portal

class SnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snapshot
        fields = ('pk','created','url','camera')

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ('pk','title')
