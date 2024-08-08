# Generated by Django 5.0.7 on 2024-08-07 22:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotels', '0004_alter_hotel_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_wifi', models.BooleanField(default=False)),
                ('has_swimming_pool', models.BooleanField(default=False)),
                ('has_conference_room', models.BooleanField(default=False)),
                ('has_tennis_court', models.BooleanField(default=False)),
                ('has_breakfast_in_bed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hotel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='facilities', to='hotels.hotel')),
            ],
            options={
                'verbose_name_plural': 'Facilities',
            },
        ),
    ]
