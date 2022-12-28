from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.page, name="page"),
    path("user/",views.user,name="user"),
    path("operator/",views.operator,name="operator"),
    path("admin/",views.admin,name="admin"),
    path("superuser/",views.superuser,name="superuser"),
]