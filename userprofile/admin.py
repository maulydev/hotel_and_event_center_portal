from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'phone_number', 'profile_picture')
    list_filter = ('user', 'phone_number')
    search_fields = ('user', 'phone_number')