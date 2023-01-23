# Generated by Django 4.1.3 on 2023-01-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_reservationdatabase_lab_station'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationdatabase',
            name='approved_status_operator',
            field=models.PositiveSmallIntegerField(choices=[(0, 'niezatwierdzona rezerwacja'), (1, 'zatwierdzona rezerwacja'), (2, 'odrzucona rezerwacja')], default=0),
        ),
    ]