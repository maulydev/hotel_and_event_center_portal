from django.contrib import admin
from .models import OtpHistory


@admin.register(OtpHistory)
class OtpHistoryAdmin(admin.ModelAdmin):

    list_display = ('user', 'otp', 'created_at', 'expires_at')
    list_filter = ('user', 'created_at', 'expires_at')
    search_fields = ('user', 'created_at', 'expires_at')
