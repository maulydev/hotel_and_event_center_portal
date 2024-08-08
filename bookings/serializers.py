from rest_framework import serializers
from .models import Booking
from userprofile.serializers import UserProfileSerializer
from rooms.serializers import RoomSerializer

class BookingSerializer(serializers.ModelSerializer):
    # user = UserProfileSerializer(read_only=True)
    # room = RoomSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = '__all__'

class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('checkin', 'checkout', 'user', 'room')