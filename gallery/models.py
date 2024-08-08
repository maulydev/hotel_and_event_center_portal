from django.db import models

class Gallery(models.Model):
    hotel = models.ForeignKey('hotels.Hotel', on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to="gallery_images/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.hotel.name
    
    class Meta:
        verbose_name_plural = "Gallery"