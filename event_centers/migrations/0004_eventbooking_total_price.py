# Generated by Django 5.0.7 on 2024-08-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_centers', '0003_remove_eventbooking_contact_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventbooking',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
