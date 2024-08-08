from rest_framework import serializers
from userprofile.serializers import UserProfileSerializer
from facilities.models import Facilities
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer(read_only=True)
    facilities = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Hotel
        fields = '__all__'
        
    def get_facilities(self, obj):
        facilities_dict = {}
        facilities = Facilities.objects.filter(hotel=obj).first()
        facilities_dict["has_wifi"] = facilities.has_wifi
        facilities_dict["has_swimming_pool"] = facilities.has_swimming_pool
        facilities_dict["has_conference_room"] = facilities.has_conference_room
        facilities_dict["has_tennis_court"] = facilities.has_tennis_court
        facilities_dict["has_breakfast_in_bed"] = facilities.has_breakfast_in_bed
        return facilities_dict