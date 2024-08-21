# Generated by Django 5.0.7 on 2024-08-21 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0008_alter_otphistory_options_otphistory_expires_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otphistory',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'OTP History'},
        ),
        migrations.RemoveField(
            model_name='otphistory',
            name='user',
        ),
        migrations.AddField(
            model_name='otphistory',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
