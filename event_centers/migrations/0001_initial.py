# Generated by Django 5.0.7 on 2024-08-22 08:51

import django.db.models.deletion
import lib.path_and_rename
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0003_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_center_number', models.CharField(blank=True, max_length=10, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to=lib.path_and_rename.EventCenterImageRename('event_center_images/'))),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=150)),
                ('region', models.CharField(choices=[('AH', 'Ashanti'), ('BA', 'Bono'), ('BE', 'Bono East'), ('AHA', 'Ahafo'), ('CP', 'Central'), ('EP', 'Eastern'), ('GP', 'Greater Accra'), ('NE', 'North East'), ('NP', 'Northern'), ('OT', 'Oti'), ('SV', 'Savannah'), ('UE', 'Upper East'), ('UW', 'Upper West'), ('VR', 'Volta'), ('WR', 'Western'), ('WN', 'Western North')], max_length=50)),
                ('country', models.CharField(choices=[('GH', 'Ghana')], default='GH', max_length=50)),
                ('contact_number', models.CharField(max_length=20)),
                ('website', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_centers', to='userprofile.userprofile')),
            ],
        ),
    ]
