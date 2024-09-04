from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer
from .models import EventCenterPayment
from .serializers import EventCenterPaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_fields = ['booking__room__hotel__hotel_number', 'booking__room__room_number', 'payment_method', 'payment_status']
    
    def perform_create(self, serializer):
        payment = serializer.save()
        if payment:
            booking = payment.booking
            booking_code = booking.booking_number
            user_phone = booking.customer.phone_number
            
            from lib.otp import send_sms
            
            message = f'Your payment for booking {booking_code} has been processed successfully. Thank you for your business!'
            send_sms(user_phone, message)
    
    

class EventCenterPaymentViewSet(viewsets.ModelViewSet):
    queryset = EventCenterPayment.objects.all()
    serializer_class = EventCenterPaymentSerializer
    filterset_fields = ['event_center_booking__event_center__event_center_number', 'payment_method', 'payment_status']
    
    def perform_create(self, serializer):
        payment = serializer.save()
        if payment:
            booking = payment.event_center_booking
            booking_code = booking.booking_number
            user_phone = booking.customer.phone_number
            
            from lib.otp import send_sms
            
            message = f'Your payment for event center booking {booking_code} has been processed successfully. Thank you for your business!'
            send_sms(user_phone, message)