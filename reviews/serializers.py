from rest_framework import serializers
from .models import Review
from userprofile.serializers import UserProfileSerializer


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
