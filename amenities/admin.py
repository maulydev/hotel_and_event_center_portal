from django.contrib import admin
from .models import Amenity

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)