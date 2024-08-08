from django.contrib import admin
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'image', 'created_at', 'updated_at')
    list_filter = ('hotel',)