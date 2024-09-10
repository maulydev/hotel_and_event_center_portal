from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    user = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE)
    hotel = models.ForeignKey('hotels.Hotel', on_delete=models.CASCADE)
    review = models.TextField()
    price_rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    service_rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    quality_rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    location_rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review
    
    
    
class EventCenterReview(models.Model):
    user = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE)
    event_center = models.ForeignKey('event_centers.EventCenter', on_delete=models.CASCADE)
    review = models.TextField()
    price_rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    service_rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    quality_rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    location_rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review