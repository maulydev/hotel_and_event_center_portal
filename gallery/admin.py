from django.contrib import admin
from .models import Gallery, EventCenterGallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'image', 'created_at', 'updated_at')
    list_filter = ('hotel',)
    


@admin.register(EventCenterGallery)
class EventCenterGalleryAdmin(admin.ModelAdmin):
    list_display = ('event_center', 'image', 'created_at', 'updated_at')
    list_filter = ('event_center',)