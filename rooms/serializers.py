from rest_framework import serializers
from bookings.models import Booking
from datetime import datetime
from .models import Room
import json

current_date = datetime.now().date()

class RoomSerializer(serializers.ModelSerializer):
    has_booking = serializers.SerializerMethodField()
    booking_list = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Room
        fields = '__all__' 
    
    def get_has_booking(self, obj):
        return Booking.objects.filter(room=obj, checkout__gte=current_date).exists()
    
    def get_booking_list(self, obj):
        bookings_dict = []
        bookings = Booking.objects.filter(room=obj)
        for booking in bookings:
            bookings_dict.append({
                "id": booking.pk,
                "booking_number": booking.booking_number,
                "checkin": booking.checkin,
                "checkout": booking.checkout,
                "created_at": booking.created_at,
                "status": booking.status,
                "total_cost": booking.total_cost,
            })
        return bookings_dict