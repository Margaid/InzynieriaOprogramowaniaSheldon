from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=30,label="nazwa")
    first_name = forms.CharField(max_length=30, required=True,label="imię")
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2',)


class ProfileForm(forms.ModelForm):
    firma = forms.CharField(help_text='Podaj firme')
    operator = forms.CharField()
    class Meta:
        model=Profile
        fields=['firma', 'operator',]