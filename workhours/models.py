from django.db import models

class Workhours(models.Model):
    hotel = models.OneToOneField('hotels.Hotel', on_delete=models.CASCADE, related_name='workhours')
    sunday = models.CharField(max_length=30, default="8:00am - 6:00pm")
    monday = models.CharField(max_length=30, default="8:00am - 6:00pm")
    tuesday = models.CharField(max_length=30, default="8:00am - 6:00pm")
    wednesday = models.CharField(max_length=30, default="8:00am - 6:00pm")
    thursday = models.CharField(max_length=30, default="8:00am - 6:00pm")
    friday = models.CharField(max_length=30, default="8:00am - 6:00pm")
    saturday = models.CharField(max_length=30, default="8:00am - 6:00pm")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.hotel.name
    
    class Meta:
        verbose_name_plural = "Working Hours"



class EventCenterWorkhours(models.Model):
    event_center = models.OneToOneField('event_centers.EventCenter', on_delete=models.CASCADE, related_name='workhours')
    sunday = models.CharField(max_length=30, default="8:00am - 6:00pm")
    monday = models.CharField(max_length=30, default="8:00am - 6:00pm")
    tuesday = models.CharField(max_length=30, default="8:00am - 6:00pm")
    wednesday = models.CharField(max_length=30, default="8:00am - 6:00pm")
    thursday = models.CharField(max_length=30, default="8:00am - 6:00pm")
    friday = models.CharField(max_length=30, default="8:00am - 6:00pm")
    saturday = models.CharField(max_length=30, default="8:00am - 6:00pm")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.event_center.name
    
    class Meta:
        verbose_name_plural = "Event Center Working Hours"