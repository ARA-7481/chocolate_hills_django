# Generated by Django 4.1.5 on 2023-01-10 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_tourists_date_time_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tourists',
            new_name='TouristLog',
        ),
        migrations.RenameModel(
            old_name='Vehicles',
            new_name='Vehicle',
        ),
        migrations.RenameField(
            model_name='vehiclelog',
            old_name='vehicles',
            new_name='vehicle',
        ),
    ]
