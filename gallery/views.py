from rest_framework import viewsets
from .models import Gallery
from .serializers import GallerySerializer

class GalleryViewset(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    filterset_fields = ['hotel__hotel_number']