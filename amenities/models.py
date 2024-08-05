from django.db import models

class Amenity(models.Model):
    hotel = models.ForeignKey('hotels.Hotel', on_delete=models.CASCADE, related_name='amenities')
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Amenities"