from rest_framework import serializers
from .models import Room
from bookings.models import Booking
from datetime import datetime

current_date = datetime.now().date()

class RoomSerializer(serializers.ModelSerializer):
    has_booking = serializers.SerializerMethodField()
    class Meta:
        model = Room
        fields = '__all__' 
    
    def get_has_booking(self, obj):
        return Booking.objects.filter(room=obj, checkout__gte=current_date).exists()