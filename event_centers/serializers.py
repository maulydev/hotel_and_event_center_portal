from rest_framework import serializers
from .models import EventCenter
from .models import EventBooking


class EventCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCenter
        fields = '__all__'  # Or specify the fields explicitly if you want to exclude/include specific fields



class EventBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventBooking
        fields = '__all__'  # Or specify the fields explicitly if you want to exclude/include specific fields
