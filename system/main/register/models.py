from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    #REQUIRED_FIELDS = []
    
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    firma = models.CharField(max_length=100, blank=True)
    operator = models.CharField(max_length=100, blank=False)

    #USERNAME_FIELD=user.username

    def __str__(self):
        return self.username
'''
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)
    instance.customuser.save()
    '''