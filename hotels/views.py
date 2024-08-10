from rest_framework import viewsets
from .models import Hotel
from .serializers import HotelSerializer
from lib.pagination import Pagination

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    # pagination_class = Pagination
    lookup_field = 'hotel_number'