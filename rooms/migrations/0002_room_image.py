# Generated by Django 5.0.7 on 2024-08-03 13:14

import lib.path_and_rename
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, upload_to=lib.path_and_rename.RoomImageRename('room_images/')),
        ),
    ]
