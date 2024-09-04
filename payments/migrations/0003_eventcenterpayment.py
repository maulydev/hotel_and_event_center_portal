# Generated by Django 5.0.7 on 2024-09-04 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_centers', '0004_eventbooking_total_price'),
        ('payments', '0002_rename_booking_id_payment_booking_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCenterPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(editable=False, max_length=20, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('card', 'Card'), ('cash', 'Cash'), ('momo', 'MoMo')], default='card', max_length=50)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event_center_booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_centers.eventbooking')),
            ],
        ),
    ]
