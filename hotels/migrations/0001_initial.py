# Generated by Django 5.0.7 on 2024-08-03 13:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_number', models.CharField(blank=True, max_length=10, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='hotel_images/')),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=150)),
                ('region', models.CharField(choices=[('AH', 'Ashanti'), ('BA', 'Bono'), ('BE', 'Bono East'), ('AHA', 'Ahafo'), ('CP', 'Central'), ('EP', 'Eastern'), ('GP', 'Greater Accra'), ('NE', 'North East'), ('NP', 'Northern'), ('OT', 'Oti'), ('SV', 'Savannah'), ('UE', 'Upper East'), ('UW', 'Upper West'), ('VR', 'Volta'), ('WR', 'Western'), ('WN', 'Western North')], max_length=50)),
                ('country', models.CharField(choices=[('GH', 'Ghana')], max_length=50)),
                ('contact_number', models.CharField(max_length=20)),
                ('website', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
