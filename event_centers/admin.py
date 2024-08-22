from django.contrib import admin
from .models import EventCenter
from .models import EventBooking

class EventCenterAdmin(admin.ModelAdmin):
    list_display = (
        'event_center_number',
        'name',
        'owner',
        'city',
        'region',
        'country',
        'contact_number',
        'created_at',
        'updated_at'
    )
    list_filter = ('region', 'country', 'created_at')
    search_fields = ('name', 'address', 'contact_number')
    ordering = ('-created_at',)
    readonly_fields = ('event_center_number', 'created_at', 'updated_at')
    
    def save_model(self, request, obj, form, change):
        # Optionally add custom save logic here
        super().save_model(request, obj, form, change)

admin.site.register(EventCenter, EventCenterAdmin)



class EventBookingAdmin(admin.ModelAdmin):
    list_display = (
        'event_center',
        'customer',
        'start_date',
        'end_date',
        'created_at',
        'updated_at'
    )
    list_filter = ('event_center', 'start_date', 'end_date')
    search_fields = ('customer__user__username', 'event_center__name')
    ordering = ('-start_date',)
    readonly_fields = ('created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        # Optionally add custom save logic here
        super().save_model(request, obj, form, change)

admin.site.register(EventBooking, EventBookingAdmin)
