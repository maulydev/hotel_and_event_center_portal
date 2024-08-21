from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

class OtpHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    def is_expired(self):
        return timezone.now() > self.expires_at

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set expiry time when creating a new OTP
            self.expires_at = timezone.now() + timedelta(minutes=10)  # Example expiry
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "OTP History"