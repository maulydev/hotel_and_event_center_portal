from rest_framework import serializers
from .models import Workhours

class WorkhoursSerializers(serializers.ModelSerializer):
    workhours = serializers.SerializerMethodField()

    class Meta:
        model = Workhours
        exclude = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    def get_workhours(self, obj):
        return [
            {"day": "Sunday", "period": obj.sunday},
            {"day": "Monday", "period": obj.monday},
            {"day": "Tuesday", "period": obj.tuesday},
            {"day": "Wednesday", "period": obj.wednesday},
            {"day": "Thursday", "period": obj.thursday},
            {"day": "Friday", "period": obj.friday},
            {"day": "Saturday", "period": obj.saturday},
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['workhours'] = self.get_workhours(instance)
        return representation
