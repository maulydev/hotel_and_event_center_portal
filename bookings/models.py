import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
class Booking(models.Model):
    booking_number = models.CharField(max_length=50, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    total_cost = models.DecimalField(decimal_places=2, max_digits=10, blank=True)
    status = models.CharField(max_length=50, default="pending", choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Hotel Booking"
        verbose_name_plural = "Hotel Bookings"

    def clean(self):
        # Exclude the current booking from the overlap check when updating
        overlapping_bookings = Booking.objects.filter(
            room=self.room,
            checkin__lt=self.checkout,
            checkout__gt=self.checkin
        ).exclude(id=self.id)

        if overlapping_bookings.exists():
            raise ValidationError("This room is already booked for the selected period.")


    def save(self, *args, **kwargs):
        self.clean()  # Ensure that the booking is valid before saving

        if self.checkout > self.checkin:
            delta = self.checkout - self.checkin
            self.total_cost = self.room.price_per_night * delta.days
        else:
            self.total_cost = self.room.price_per_night
            
        if not self.booking_number:
            # Generate a random unique booking number
            self.booking_number = str(uuid.uuid4()).replace('-', '').upper()[:10]  # Take the first 10 characters

        super(Booking, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.booking_number
