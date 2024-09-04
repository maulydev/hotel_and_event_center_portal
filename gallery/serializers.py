from rest_framework import serializers
from .models import Gallery, EventCenterGallery


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
        


class EventCenterGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCenterGallery
        fields = '__all__'