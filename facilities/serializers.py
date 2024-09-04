from rest_framework import serializers
from .models import Facilities, EventCenterFacilities


class FacilitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = '__all__'
        
        

class EventCenterFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCenterFacilities
        fields = '__all__'