# Generated by Django 5.0.7 on 2024-08-07 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workhours', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workhours',
            options={'verbose_name_plural': 'Working Hours'},
        ),
        migrations.AlterField(
            model_name='workhours',
            name='friday',
            field=models.CharField(default='8:00am - 6:00pm', max_length=30),
        ),
        migrations.AlterField(
            model_name='workhours',
            name='monday',
            field=models.CharField(default='8:00am - 6:00pm', max_length=30),
        ),
        migrations.AlterField(
            model_name='workhours',
            name='saturday',
            field=models.CharField(default='8:00am - 6:00pm', max_length=30),
        ),
        migrations.AlterField(
            model_name='workhours',
            name='sunday',
            field=models.CharField(default='8:00am - 6:00pm', max_length=30),
        ),
        migrations.AlterField(
            model_name='workhours',
            name='thursday',
            field=models.CharField(default='8:00am - 6:00pm', max_length=30),
        ),
        migrations.AlterField(
            model_name='workhours',
            name='tuesday',
            field=models.CharField(default='8:00am - 6:00pm', max_length=30),
        ),
        migrations.AlterField(
            model_name='workhours',
            name='wednesday',
            field=models.CharField(default='8:00am - 6:00pm', max_length=30),
        ),
    ]
