from rest_framework import serializers
from .models import Payment
from bookings.serializers import BookingSerializer

class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(read_only=True)
    class Meta:
        model = Payment
        fields = '__all__'