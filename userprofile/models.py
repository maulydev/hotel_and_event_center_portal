from django.contrib.auth.models import User
from django.db import models
from lib.path_and_rename import ProfileImageRename

profile_image_rename = ProfileImageRename('profile_pics/')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    role = models.CharField(max_length=50, default="user")
    phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to=profile_image_rename, blank=True)

    def __str__(self):
        return self.user.username