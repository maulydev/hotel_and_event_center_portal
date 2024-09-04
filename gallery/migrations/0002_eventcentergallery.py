# Generated by Django 5.0.7 on 2024-09-04 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_centers', '0004_eventbooking_total_price'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCenterGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='event_center_gallery_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='event_centers.eventcenter')),
            ],
            options={
                'verbose_name_plural': 'Event Center Gallery',
            },
        ),
    ]