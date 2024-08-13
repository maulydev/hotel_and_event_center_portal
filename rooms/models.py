from django.db import models
from hotels.models import Hotel
from lib.path_and_rename import RoomImageRename

room_image_rename = RoomImageRename("room_images/")

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=150)
    image = models.ImageField(upload_to=room_image_rename, blank=True)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
        
    def __str__(self) -> str:
        return self.room_number