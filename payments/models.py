import uuid
from django.db import models
from django.utils.timezone import now

PAYMENT_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('cancelled', 'Cancelled'),
)

PAYMENT_METHOD_CHOICES = (
    ('card', 'Card'),
    ('cash', 'Cash'),
    ('momo', 'MoMo'),
)

class Payment(models.Model):
    payment_id = models.CharField(max_length=20, unique=True, editable=False)
    booking = models.ForeignKey('bookings.Booking', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, default="card", choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=50, default="pending", choices=PAYMENT_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.payment_id:
            self.payment_id = self.generate_payment_id()
        super().save(*args, **kwargs)
        
        if self.payment_status == 'confirmed':
            self.booking.status = 'confirmed'
            self.booking.save()

    def generate_payment_id(self):
        # Generate a unique ID based on UUID and current timestamp
        unique_id = uuid.uuid4().hex[:6].upper()
        timestamp = now().strftime('%Y%m%d%H%M%S')
        payment_id = f'PAY-{timestamp}-{unique_id}'
        
        # Ensure the payment_id is unique
        while Payment.objects.filter(payment_id=payment_id).exists():
            unique_id = uuid.uuid4().hex[:6].upper()
            payment_id = f'PAY-{timestamp}-{unique_id}'
        
        return payment_id

    def __str__(self):
        return self.payment_id




class EventCenterPayment(models.Model):
    payment_id = models.CharField(max_length=20, unique=True, editable=False)
    event_center_booking = models.ForeignKey('event_centers.EventBooking', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, default="card", choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=50, default="confirmed", choices=PAYMENT_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.payment_id:
            self.payment_id = self.generate_payment_id()
        super().save(*args, **kwargs)
        
        if self.payment_status == 'confirmed':
            self.event_center_booking.status = 'confirmed'
            self.event_center_booking.save()


    def generate_payment_id(self):
        # Generate a unique ID based on UUID and current timestamp
        unique_id = uuid.uuid4().hex[:6].upper()
        timestamp = now().strftime('%Y%m%d%H%M%S')
        payment_id = f'ECPAY-{timestamp}-{unique_id}'
        
        # Ensure the payment_id is unique
        while EventCenterPayment.objects.filter(payment_id=payment_id).exists():
            unique_id = uuid.uuid4().hex[:6].upper()
            payment_id = f'ECPAY-{timestamp}-{unique_id}'
        
        return payment_id

    def __str__(self):
        return self.payment_id