from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer, BookingCreateSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    filterset_fields = ['booking_number','room__room_number', 'room__hotel__hotel_number', 'status']
    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return BookingCreateSerializer
        return BookingSerializer