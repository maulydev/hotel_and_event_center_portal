from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer
from .models import EventCenterPayment
from .serializers import EventCenterPaymentSerializer
from lib.otp import send_sms

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_fields = ['booking__room__hotel__hotel_number', 'booking__room__room_number', 'payment_method', 'payment_status']

    def perform_create(self, serializer):
        payment = serializer.save()
        if payment.payment_status == 'confirmed':
            # Assuming the booking has a related user with a phone number
            phone_number = payment.booking.user.profile.phone_number
            message = f"Your payment of {payment.amount} for booking {payment.booking.booking_number} was successful."
            send_sms(phone_number, message)
    
    

class EventCenterPaymentViewSet(viewsets.ModelViewSet):
    queryset = EventCenterPayment.objects.all()
    serializer_class = EventCenterPaymentSerializer
    filterset_fields = ['event_center_booking__event_center__event_center_number', 'payment_method', 'payment_status']

    def perform_create(self, serializer):
        payment = serializer.save()
        if payment.payment_status == 'confirmed':
            phone_number = payment.event_center_booking.customer.phone_number
            message = f"Your payment of {payment.amount} for event center booking {payment.event_center_booking.booking_number} was successful."
            send_sms(phone_number, message)