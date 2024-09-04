from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import EventCenter, EventBooking
from .serializers import EventCenterSerializer, EventBookingSerializer, EventBookingCreateSerializer

class EventCenterViewSet(viewsets.ModelViewSet):
    queryset = EventCenter.objects.all()
    serializer_class = EventCenterSerializer
    lookup_field = 'event_center_number'
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'region', 'city', 'country']
    search_fields = ['name', 'region', 'city', 'country']
    

    def get_queryset(self):
        return EventCenter.objects.all()

class EventBookingViewSet(viewsets.ModelViewSet):
    queryset = EventBooking.objects.all()
    filterset_fields = ['booking_number', 'event_center__event_center_number', 'status']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['booking_number', 'event_center__name']

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return EventBookingCreateSerializer
        return EventBookingSerializer