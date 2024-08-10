from rest_framework import serializers
from userprofile.serializers import UserProfileSerializer
from facilities.models import Facilities
from reviews.models import Review
from django.db.models import Avg
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer(read_only=True)
    facilities = serializers.SerializerMethodField(read_only=True)
    avg_ratings = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Hotel
        fields = '__all__'
        
    def get_facilities(self, obj):
        facilities = Facilities.objects.filter(hotel=obj).values_list(
            'has_wifi', 'has_swimming_pool', 'has_conference_room', 
            'has_tennis_court', 'has_breakfast_in_bed'
        ).first()
        if facilities:
            return {
                "has_wifi": facilities[0],
                "has_swimming_pool": facilities[1],
                "has_conference_room": facilities[2],
                "has_tennis_court": facilities[3],
                "has_breakfast_in_bed": facilities[4],
            }
        return {}

    def get_avg_ratings(self, obj):
        avg_ratings = Review.objects.filter(hotel=obj).aggregate(
            average_price_rating=Avg('price_rating'),
            average_location_rating=Avg('location_rating'),
            average_quality_rating=Avg('quality_rating'),
            average_service_rating=Avg('service_rating')
        )
        return avg_ratings if any(avg_ratings.values()) else {}
