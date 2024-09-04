from django.contrib import admin
from .models import Facilities, EventCenterFacilities

@admin.register(Facilities)
class FacilitiesAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'has_wifi', 'has_swimming_pool', 'has_conference_room', 'has_tennis_court', 'has_breakfast_in_bed')
    list_filter = ('hotel',)
    

@admin.register(EventCenterFacilities)
class EventCenterFacilitiesAdmin(admin.ModelAdmin):
    list_display = ('event_center', 'has_wifi', 'has_swimming_pool', 'has_conference_room', 'has_tennis_court')
    list_filter = ('event_center',)
