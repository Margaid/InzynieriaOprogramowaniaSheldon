from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=30, label="")
    username.widget.attrs.update({'placeholder': 'nazwa'})
    first_name = forms.CharField(max_length=30, required=True,label="")
    first_name.widget.attrs.update({'placeholder': 'imię'})
    last_name = forms.CharField(max_length=30, required=True,label="")
    last_name.widget.attrs.update({'placeholder': 'nazwisko'},label="")
    email = forms.EmailField(max_length=254, label="")
    email.widget.attrs.update({'placeholder': 'e-mail'},label="")
    


    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2',)
        

class ProfileForm(forms.ModelForm):
    firma = forms.CharField(label="")
    firma.widget.attrs.update({'placeholder': 'firma'})
    class Meta:
        model=Profile
        fields=['firma',]