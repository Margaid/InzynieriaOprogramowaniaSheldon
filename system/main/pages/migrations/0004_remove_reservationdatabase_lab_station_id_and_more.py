# Generated by Django 4.1.3 on 2023-01-16 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_reservationdatabase_operator_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservationdatabase',
            name='lab_station_id',
        ),
        migrations.RemoveField(
            model_name='reservationdatabase',
            name='reservation_date',
        ),
    ]
