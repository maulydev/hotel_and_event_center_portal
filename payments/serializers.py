from rest_framework import serializers
from .models import Payment, EventCenterPayment
from bookings.serializers import BookingSerializer
import datetime

class PaymentSerializer(serializers.ModelSerializer):
    # booking = BookingSerializer(read_only=True)
    class Meta:
        model = Payment
        fields = '__all__'

    def create(self, validated_data):
        payment = Payment.objects.create(**validated_data)
        payment.payment_status = 'confirmed'
        payment.save()
        return payment
    
class EventCenterPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCenterPayment
        fields = '__all__'

    def create(self, validated_data):
        payment = EventCenterPayment.objects.create(**validated_data)
        return payment