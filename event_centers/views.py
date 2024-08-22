from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import EventCenter, EventBooking
from .serializers import EventCenterSerializer, EventBookingSerializer

class EventCenterViewSet(viewsets.ModelViewSet):
    queryset = EventCenter.objects.all()
    serializer_class = EventCenterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'region', 'city', 'country']

    def get_queryset(self):
        return EventCenter.objects.all()

class EventBookingViewSet(viewsets.ModelViewSet):
    queryset = EventBooking.objects.all()
    serializer_class = EventBookingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['event_center', 'customer', 'start_date', 'end_date']

    def get_queryset(self):
        return EventBooking.objects.all()

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.profile)  # Assuming the user has a profile
