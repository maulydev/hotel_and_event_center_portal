# from rest_framework import serializers

# class RegisterSerializer(serializers.Serializer):
#     phone_number = serializers.CharField(required=True)
#     username = serializers.CharField(required=False)  # Not required for OTP generation
#     otp = serializers.CharField(required=False)  # Not required for OTP generation

from rest_framework import serializers
from .models import OtpHistory
from django.contrib.auth.models import User

class OtpGenerationSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)

class OtpVerificationSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    otp = serializers.CharField(required=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class OtpHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpHistory
        fields = ['phone_number', 'otp', 'created_at', 'expires_at']
        read_only_fields = ['created_at', 'expires_at']