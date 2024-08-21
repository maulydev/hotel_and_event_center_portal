from django.contrib import admin
from .models import OtpHistory


@admin.register(OtpHistory)
class OtpHistoryAdmin(admin.ModelAdmin):

    list_display = ('phone_number', 'otp', 'created_at', 'expires_at')
    list_filter = ('phone_number', 'created_at', 'expires_at')
    search_fields = ('phone_number', 'created_at', 'expires_at')
