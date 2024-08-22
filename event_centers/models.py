from django.db import models, transaction
from decimal import Decimal
from django.utils import timezone
from lib.path_and_rename import EventCenterImageRename
from lib.constants import COUNTRY_CHOICES, REGION_CHOICES


event_center_image_rename = EventCenterImageRename("event_center_images/")

class EventCenter(models.Model):
    event_center_number = models.CharField(max_length=10, unique=True, blank=True)
    owner = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='event_centers')
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to=event_center_image_rename, blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=150)
    number_of_occupants = models.IntegerField(default=0)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    region = models.CharField(max_length=50, choices=REGION_CHOICES)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default="GH")
    contact_number = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.event_center_number:
            with transaction.atomic():
                last_center = EventCenter.objects.all().order_by('id').last()
                if not last_center:
                    new_number = 1
                else:
                    last_number_str = last_center.event_center_number.replace('EVT', '')
                    try:
                        last_number = int(last_number_str)
                        new_number = last_number + 1
                    except ValueError:
                        new_number = 1
                self.event_center_number = f'EVT{new_number:05d}'
        super(EventCenter, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name



class EventBooking(models.Model):
    event_center = models.ForeignKey(EventCenter, on_delete=models.CASCADE, related_name='event_bookings')
    customer = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Booking by {self.customer.user.username} at {self.event_center.name} from {self.start_date} to {self.end_date}"

    def save(self, *args, **kwargs):
        if not self.total_price:  # Only calculate price if it's the first save (total_price is None)
            if self.start_date < timezone.now():
                raise ValueError("The booking start date cannot be in the past.")
            if self.start_date >= self.end_date:
                raise ValueError("The end date must be after the start date.")
            
            # Calculate the duration in hours
            duration = self.end_date - self.start_date
            hours = Decimal(duration.total_seconds() / 3600)
            
            # Calculate the total price
            self.total_price = hours * self.event_center.price_per_hour
        
        super(EventBooking, self).save(*args, **kwargs)
