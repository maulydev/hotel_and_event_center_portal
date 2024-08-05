from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import Hotel
from .serializers import HotelSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer