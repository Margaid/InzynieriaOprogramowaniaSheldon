from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Profile(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #dodanie pola firma do modelu użytkownika
    firma = models.CharField(max_length=100, blank=True,help_text='test')
    #dodanie pola operatora do modelu użytkownika
    operator = models.CharField(max_length=100, blank=False)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

     
@receiver(post_save, sender=User)
def update_user_customuser(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)   
    instance.profile.save()



   