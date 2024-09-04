from rest_framework import serializers
from .models import Booking
from userprofile.serializers import UserProfileSerializer
from rooms.serializers import RoomSerializer
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class BookingSerializer(serializers.ModelSerializer):
    # user = UserProfileSerializer(read_only=True)
    # room = RoomSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = '__all__'

class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'total_cost', 'checkin', 'checkout', 'room', 'user')

    def validate(self, data):
        checkin = data.get('checkin')
        checkout = data.get('checkout')
        room = data.get('room')
        
        # Check for overlapping bookings
        overlapping_bookings = Booking.objects.filter(
            room=room,
            checkout__gt=checkin,
            checkin__lt=checkout
        )

        if overlapping_bookings.exists():
            raise ValidationError(_("This room is already booked for the selected period."))
        
        return data