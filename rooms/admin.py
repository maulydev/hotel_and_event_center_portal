from django.contrib import admin
from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'room_number', 'room_type', 'description', 'price_per_night', 'is_available')
    list_filter = ('hotel', 'room_type')
    search_fields = ('hotel', 'room_number', 'room_type')

    def is_available(self, obj):
        return obj.is_available
