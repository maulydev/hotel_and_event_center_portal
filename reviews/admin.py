from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'review', 'rating', 'created_at', 'updated_at')
    list_filter = ('user', 'hotel', 'rating')
    search_fields = ('user__username', 'hotel', 'rating')