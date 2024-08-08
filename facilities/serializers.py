from rest_framework import serializers
from .models import Facilities


class FacilitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = '__all__'