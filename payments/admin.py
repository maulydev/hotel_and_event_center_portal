from django.contrib import admin
from .models import Payment, EventCenterPayment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'booking', 'amount', 'payment_method', 'payment_status', 'created_at', 'updated_at')
    list_filter = ('booking', 'payment_method', 'payment_status')
    search_fields = ('booking', 'payment_method', 'payment_status')
    

@admin.register(EventCenterPayment)
class EventCenterPaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'event_center_booking', 'amount', 'payment_method', 'payment_status', 'created_at', 'updated_at')
    list_filter = ('event_center_booking', 'payment_method', 'payment_status')
    search_fields = ('event_center_booking', 'payment_method', 'payment_status')