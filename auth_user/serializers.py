from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    username = serializers.CharField(required=False)  # Not required for OTP generation
    otp = serializers.CharField(required=False)  # Not required for OTP generation
