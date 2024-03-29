from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # dodanie pola firma do modelu użytkownika
    firm = models.CharField(max_length=100, blank=True)

    # lista operatorów do wyboru
    OPERATORS = (
        ('operator1', 'operator maszyny 1'),
        ('operator2', 'operator maszyny 2'),
    )
    # dodanie pola operatora do modelu użytkownika
    operator = models.CharField(max_length=100, choices=OPERATORS, blank=True)

    NOT_APPROVED = 0
    APPROVED = 1
    REJECTED = 2
    # status użytkownika
    STATUS = (
        (NOT_APPROVED, ('niezatwierdzony użytkownik')),
        (APPROVED, ('zatwierdzony użytkownik')),
        (REJECTED, ('odrzucony użytkownik'))

    )
    approval = models.PositiveSmallIntegerField(
        choices=STATUS, default=NOT_APPROVED)

    # rodzaj konta
    is_user = models.BooleanField(default=True)
    is_operator = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def update_user_customuser(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
