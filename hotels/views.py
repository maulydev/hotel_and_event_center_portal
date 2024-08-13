from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Hotel
from .serializers import HotelSerializer
from lib.pagination import Pagination
from django_filters.rest_framework import DjangoFilterBackend as Filterset

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    pagination_class = Pagination
    lookup_field = 'hotel_number'
    filterset_fields = ['city', 'region']
    filter_backends = [SearchFilter, Filterset]
    search_fields = ['name', 'city', 'region']