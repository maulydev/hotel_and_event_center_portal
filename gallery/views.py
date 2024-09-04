from rest_framework import viewsets
from .models import Gallery, EventCenterGallery
from .serializers import GallerySerializer, EventCenterGallerySerializer


class GalleryViewset(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    filterset_fields = ['hotel__hotel_number']


class EventCenterGalleryViewset(viewsets.ModelViewSet):
    queryset = EventCenterGallery.objects.all()
    serializer_class = EventCenterGallerySerializer
    filterset_fields = ['event_center__event_center_number']