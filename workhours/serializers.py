from rest_framework import serializers
from .models import Workhours


class WorkhoursSerializers(serializers.ModelSerializer):
    class Meta:
        model = Workhours
        fields = '__all__'