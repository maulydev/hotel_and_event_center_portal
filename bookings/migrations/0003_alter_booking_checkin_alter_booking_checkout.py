# Generated by Django 5.0.7 on 2024-08-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_alter_booking_status_alter_booking_total_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout',
            field=models.DateTimeField(),
        ),
    ]
