from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_number', 'user', 'room', 'checkin', 'checkout', 'total_cost', 'status', 'created_at', 'updated_at')
    list_filter = ('user', 'room', 'status')
    search_fields = ('booking_number', 'user__username', 'room__room_number', 'status')
    readonly_fields = ('booking_number', 'total_cost')