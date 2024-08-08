from django.contrib import admin
from .models import Workhours


@admin.register(Workhours)
class WorkhoursAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
    list_filter = ('hotel',)