from rest_framework import viewsets
from .models import Amenity
from .serializers import AmenitySerializer

class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    filterset_fields = ['hotel__hotel_number']