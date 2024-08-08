from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'review', 'quality_rating', 'location_rating', 'service_rating', 'price_rating', 'created_at', 'updated_at')
    list_filter = ('user', 'hotel', 'quality_rating', 'location_rating', 'service_rating', 'price_rating',)
    search_fields = ('user__username', 'hotel', 'quality_rating', 'location_rating', 'service_rating', 'price_rating',)