from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hotel')
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=150)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name