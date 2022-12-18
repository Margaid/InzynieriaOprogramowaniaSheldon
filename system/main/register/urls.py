from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .forms import AuthForm

urlpatterns = [
    path("",views.home,name="home"),
    path("register/",views.register,name="register"),
    path("login/",auth_views.LoginView.as_view(authentication_form=AuthForm), name='login'),
    path("register/waiting/",views.waiting),
]
