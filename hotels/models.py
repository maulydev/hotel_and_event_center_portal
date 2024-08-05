from django.db import models, transaction
from lib.path_and_rename import HotelImageRename

REGION_CHOICES = (
    ('AH', 'Ashanti'),
    ('BA', 'Bono'),
    ('BE', 'Bono East'),
    ('AHA', 'Ahafo'),
    ('CP', 'Central'),
    ('EP', 'Eastern'),
    ('GP', 'Greater Accra'),
    ('NE', 'North East'),
    ('NP', 'Northern'),
    ('OT', 'Oti'),
    ('SV', 'Savannah'),
    ('UE', 'Upper East'),
    ('UW', 'Upper West'),
    ('VR', 'Volta'),
    ('WR', 'Western'),
    ('WN', 'Western North')
)

COUNTRY_CHOICES = (
    ('GH', 'Ghana'),
)

hotel_image_rename = HotelImageRename("hotel_images/")

class Hotel(models.Model):
    hotel_number = models.CharField(max_length=10, unique=True, blank=True)
    owner = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='hotels')
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to=hotel_image_rename, blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=150)
    region = models.CharField(max_length=50, choices=REGION_CHOICES)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default="GH")
    contact_number = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.hotel_number:
            with transaction.atomic():
                last_hotel = Hotel.objects.all().order_by('id').last()
                if not last_hotel:
                    new_number = 1
                else:
                    last_number_str = last_hotel.hotel_number.replace('HTL', '')
                    try:
                        last_number = int(last_number_str)
                        new_number = last_number + 1
                    except ValueError:
                        new_number = 1
                self.hotel_number = f'HTL{new_number:05d}'
        super(Hotel, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name