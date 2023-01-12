from django.db import models
from register.models import Profile
from django.contrib.auth.models import User
# Create your models here.


class ReservationDataBase(models.Model):
    lab_station = models.CharField(max_length=100)
    reservation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lab_station_id = models.IntegerField()
    approved_status = models.BooleanField(default=False)
    reservation_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # lista operatorów do wyboru
    OPERATORS = (
        ('operator1', 'operator maszyny 1'),
        ('operator2', 'operator maszyny 2'),
    )
    # dodanie pola operatora do modelu użytkownika
    operator = models.CharField(max_length=100, choices=OPERATORS, blank=True)

    def __str__(self):
        return f'{self.lab_station} Profile'


class Permissions(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    lab_station = models.ForeignKey(
        ReservationDataBase, on_delete=models.CASCADE)


class LabStation(models.Model):
    lab_name = models.CharField(max_length=100)
    lab_station = models.ForeignKey(
        ReservationDataBase, on_delete=models.CASCADE)
    room = models.CharField(max_length=10)
