from rest_framework import serializers
from .models import EventCenter
from .models import EventBooking
from userprofile.serializers import UserProfileSerializer
from facilities.models import EventCenterFacilities
from reviews.models import EventCenterReview
from django.db.models import Avg


class EventCenterSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer(read_only=True)
    facilities = serializers.SerializerMethodField(read_only=True)
    avg_ratings = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = EventCenter
        fields = '__all__'
        
    def get_facilities(self, obj):
        facilities = EventCenterFacilities.objects.filter(event_center=obj).values_list(
            'has_wifi', 'has_swimming_pool', 'has_conference_room', 
            'has_tennis_court'
        ).first()
        if facilities:
            return {
                "has_wifi": facilities[0],
                "has_swimming_pool": facilities[1],
                "has_conference_room": facilities[2],
                "has_tennis_court": facilities[3],
            }
        return {}

    def get_avg_ratings(self, obj):
        avg_ratings = EventCenterReview.objects.filter(event_center=obj).aggregate(
            average_price_rating=Avg('price_rating'),
            average_location_rating=Avg('location_rating'),
            average_quality_rating=Avg('quality_rating'),
            average_service_rating=Avg('service_rating')
        )
        return avg_ratings if any(avg_ratings.values()) else {}



class EventBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventBooking
        fields = '__all__'  # Or specify the fields explicitly if you want to exclude/include specific fields
