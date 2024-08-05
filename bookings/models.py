import uuid
from django.db import models, transaction

class Booking(models.Model):
    booking_number = models.CharField(max_length=50, unique=True, blank=True)
    user = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE)
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    total_cost = models.DecimalField(decimal_places=2, max_digits=10, blank=True)
    status = models.CharField(max_length=50, default="pending", choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
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
