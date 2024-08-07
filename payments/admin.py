from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'booking', 'amount', 'payment_method', 'payment_status', 'created_at', 'updated_at')
    list_filter = ('booking', 'payment_method', 'payment_status')
    search_fields = ('booking', 'payment_method', 'payment_status')