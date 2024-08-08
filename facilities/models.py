from django.db import models


class Facilities(models.Model):
    hotel = models.OneToOneField('hotels.Hotel', on_delete=models.CASCADE, related_name='facilities')
    has_wifi = models.BooleanField(default=False)
    has_swimming_pool = models.BooleanField(default=False)
    has_conference_room = models.BooleanField(default=False)
    has_tennis_court = models.BooleanField(default=False)
    has_breakfast_in_bed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.hotel.name
    
    class Meta:
        verbose_name_plural = "Facilities"
    
