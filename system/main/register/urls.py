from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .forms import AuthForm
from django.contrib.auth.views import LogoutView
import main.settings as settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("",views.home,name="home"),
    path("register/",views.register,name="register"),
    path("login/",auth_views.LoginView.as_view(authentication_form=AuthForm), name='login'),
    path("logout/",LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name="logout"),
    path("register/waiting/",views.waiting, name="waiting"),
    path("register/rodo/",views.rodo,name="rodo"),
]

urlpatterns += staticfiles_urlpatterns()