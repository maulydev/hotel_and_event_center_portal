from django.contrib import admin
from .models import Facilities

@admin.register(Facilities)
class FacilitiesAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'has_wifi', 'has_swimming_pool', 'has_conference_room', 'has_tennis_court', 'has_breakfast_in_bed')
    list_filter = ('hotel',)