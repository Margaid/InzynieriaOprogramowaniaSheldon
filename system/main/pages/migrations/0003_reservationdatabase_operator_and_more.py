# Generated by Django 4.1.3 on 2023-01-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_reservationdatabase_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationdatabase',
            name='operator',
            field=models.CharField(blank=True, choices=[('operator1', 'operator maszyny 1'), ('operator2', 'operator maszyny 2')], max_length=100),
        ),
        migrations.AlterField(
            model_name='labstation',
            name='lab_station',
            field=models.CharField(choices=[('1A', 'sala1'), ('2B', 'sala2'), ('3C', 'sala3'), ('4D', 'sala4')], max_length=100),
        ),
        migrations.AlterField(
            model_name='permissions',
            name='lab_station',
            field=models.CharField(choices=[('1A', 'sala1'), ('2B', 'sala2'), ('3C', 'sala3'), ('4D', 'sala4')], max_length=100),
        ),
        migrations.AlterField(
            model_name='reservationdatabase',
            name='approved_status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'niezatwierdzona rezerwacja'), (1, 'zatwierdzona rezerwacja'), (2, 'odrzucona rezerwacja')], default=0),
        ),
    ]
