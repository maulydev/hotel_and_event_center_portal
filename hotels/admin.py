from django.contrib import admin
from .models import Hotel

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'city', 'region', 'country', 'contact_number', 'website')
    list_filter = ('city', 'region', 'country')
    search_fields = ('name', 'city', 'region', 'country', 'contact_number')