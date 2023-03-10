# Generated by Django 4.1.5 on 2023-01-10 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_tourists_touristlog_rename_vehicles_vehicle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='TouristLog',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True)
        ),
        migrations.AlterField(
            model_name='VehicleLog',
            name='date',
            field=models.DateField(auto_now_add=True)
        ),
        migrations.AlterField(
            model_name='VehicleLog',
            name='time',
            field=models.TimeField(auto_now_add=True)
        ),
    ]
