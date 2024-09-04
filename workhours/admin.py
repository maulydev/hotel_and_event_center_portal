from django.contrib import admin
from .models import Workhours, EventCenterWorkhours


@admin.register(Workhours)
class WorkhoursAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
    list_filter = ('hotel',)


@admin.register(EventCenterWorkhours)
class EventCenterWorkhoursAdmin(admin.ModelAdmin):
    list_display = ('event_center', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
    list_filter = ('event_center',)