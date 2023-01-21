from django.contrib import admin
from .models import ReservationDataBase, LabStation, Permissions
# Register your models here.
admin.site.register(ReservationDataBase)
admin.site.register(LabStation)
admin.site.register(Permissions)
