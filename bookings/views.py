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

    def perform_create(self, serializer):
        booking = serializer.save()
        if booking:
            # Assuming the booking code is the booking_number
            booking_code = booking.booking_number
            user_phone = booking.user.phone_number  # Assuming user has a phone_number field
            
            # Import the send_otp_sms function
            from lib.otp import send_sms
            
            # Send the booking code to the user
            message = f'Your booking is successful. Your booking code is: {booking_code}'
            send_sms(user_phone, message)