# Generated by Django 5.0.7 on 2024-08-05 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookings', '0002_alter_booking_status_alter_booking_total_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(editable=False, max_length=20, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=50)),
                ('payment_status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.booking')),
            ],
        ),
    ]
