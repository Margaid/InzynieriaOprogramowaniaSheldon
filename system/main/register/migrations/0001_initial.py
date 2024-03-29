# Generated by Django 4.1.3 on 2022-12-29 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm', models.CharField(blank=True, max_length=100)),
                ('operator', models.CharField(blank=True, choices=[('operator1', 'operator maszyny 1'), ('operator2', 'operator maszyny 2')], max_length=100)),
                ('approval', models.PositiveSmallIntegerField(choices=[(0, 'niezatwierdzony użytkownik'), (1, 'zatwierdzony użytkownik'), (2, 'odrzucony użytkownik')], default=0)),
                ('is_user', models.BooleanField(default=True)),
                ('is_operator', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
