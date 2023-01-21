from django.db import models
from register.models import Profile
from django.contrib.auth.models import User
# Create your models here.

LAB_STATIONS = (
    ('1A', 'sala1'),
    ('2B', 'sala2'),
    ('3C', 'sala3'),
    ('4D', 'sala4'),

)


class ReservationDataBase(models.Model):
    lab_station = models.CharField(max_length=100)
    reservation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # lab_station_id = models.IntegerField()

    NOT_APPROVED = 0
    APPROVED = 1
    REJECTED = 2
    # status rezerwacji
    STATUS = (
        (NOT_APPROVED, ('niezatwierdzona rezerwacja')),
        (APPROVED, ('zatwierdzona rezerwacja')),
        (REJECTED, ('odrzucona rezerwacja'))
    )
    approved_status = models.PositiveSmallIntegerField(
        choices=STATUS, default=NOT_APPROVED)  # zrobione
    # reservation_date = models.DateTimeField()
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
    lab_station = models.CharField(
        max_length=100, choices=LAB_STATIONS)


class LabStation(models.Model):
    lab_name = models.CharField(max_length=100)
    lab_station = models.CharField(
        max_length=100, choices=LAB_STATIONS)
    room = models.CharField(max_length=10)
