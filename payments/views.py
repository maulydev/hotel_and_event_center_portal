from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer
from .models import EventCenterPayment
from .serializers import EventCenterPaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_fields = ['booking__room__hotel__hotel_number', 'booking__room__room_number', 'payment_method', 'payment_status']
    
    

class EventCenterPaymentViewSet(viewsets.ModelViewSet):
    queryset = EventCenterPayment.objects.all()
    serializer_class = EventCenterPaymentSerializer
    filterset_fields = ['event_center_booking__event_center__event_center_number', 'payment_method', 'payment_status']