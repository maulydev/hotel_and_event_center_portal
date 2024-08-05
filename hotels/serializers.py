from rest_framework import serializers
from .models import Hotel
from userprofile.serializers import UserProfileSerializer

class HotelSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer(read_only=True)
    class Meta:
        model = Hotel
        fields = '__all__'