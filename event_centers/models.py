from django.db import models, transaction
from decimal import Decimal
from django.utils import timezone
from lib.path_and_rename import EventCenterImageRename
from lib.constants import COUNTRY_CHOICES, REGION_CHOICES
from django.core.exceptions import ValidationError
import uuid
from django.contrib.auth.models import User



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
    booking_number = models.CharField(max_length=50, unique=True, blank=True)
    event_center = models.ForeignKey(EventCenter, on_delete=models.CASCADE, related_name='event_bookings')
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=50, default="pending", choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Event Center Booking"
        verbose_name_plural = "Event Center Bookings"

    def __str__(self) -> str:
        return f"Booking {self.booking_number} by {self.customer.user.username} at {self.event_center.name}"

    def clean(self):
        # Exclude the current booking from the overlap check when updating
        overlapping_bookings = EventBooking.objects.filter(
            event_center=self.event_center,
            start_date__lt=self.end_date,
            end_date__gt=self.start_date
        ).exclude(id=self.id)

        if overlapping_bookings.exists():
            raise ValidationError("This event center is already booked for the selected period.")

    def save(self, *args, **kwargs):
        self.clean()  # Ensure that the booking is valid before saving

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

        if not self.booking_number:
            # Generate a random unique booking number
            self.booking_number = f"EVB{str(uuid.uuid4()).replace('-', '').upper()[:7]}"

        super(EventBooking, self).save(*args, **kwargs)
