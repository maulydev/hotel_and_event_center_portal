from rest_framework import serializers
from .models import Amenity
from hotels.serializers import HotelSerializer
from django.utils.translation import gettext_lazy as _

class AmenitySerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)
    class Meta:
        model = Amenity
        fields = '__all__'