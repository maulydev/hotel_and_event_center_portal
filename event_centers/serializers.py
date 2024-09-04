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


class EventBookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventBooking
        fields = ('id', 'total_price', 'start_date', 'end_date', 'event_center', 'customer')

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        event_center = data.get('event_center')
        
        if start_date >= end_date:
            raise serializers.ValidationError("The end date must be after the start date.")

        # Check for overlapping bookings
        overlapping_bookings = EventBooking.objects.filter(
            event_center=event_center,
            start_date__lt=end_date,
            end_date__gt=start_date
        )

        if overlapping_bookings.exists():
            raise serializers.ValidationError("This event center is already booked for the selected period.")
        
        return data

    def create(self, validated_data):
        # Calculate total price based on event center's price per hour and booking duration
        event_center = validated_data['event_center']
        start_date = validated_data['start_date']
        end_date = validated_data['end_date']
        
        duration = end_date - start_date
        hours = duration.total_seconds() / 3600
        total_price = event_center.price_per_hour * hours
        
        validated_data['total_price'] = total_price
        
        return super().create(validated_data)