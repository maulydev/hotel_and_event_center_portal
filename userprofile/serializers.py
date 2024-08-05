from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    joined_since = serializers.ReadOnlyField(source='user.date_joined')
    class Meta:
        model = UserProfile
        fields = '__all__'