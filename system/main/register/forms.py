from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

#formularz logowania
class AuthForm(AuthenticationForm):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'validate','placeholder': 'Nazwa użytkownika'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':'Hasło'}))

#formularz rejestracji 
class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=30, label="")
    username.widget.attrs.update({'placeholder': 'Nazwa użytkownika'})
    first_name = forms.CharField(max_length=30, required=True,label="")
    first_name.widget.attrs.update({'placeholder': 'Imię'})
    last_name = forms.CharField(max_length=30, required=True,label="")
    last_name.widget.attrs.update({'placeholder': 'Nazwisko'},label="")
    email = forms.EmailField(max_length=254, label="")
    email.widget.attrs.update({'placeholder': 'E-mail'},label="")
    password1 = forms.CharField(max_length=32, label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło (max 32 znaki)'}))
    password2 = forms.CharField(max_length=32, label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Potwierdź hasło'}))


    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2',)
        
#dodatkowe pole do formularzu rejestracji      
class ProfileForm(forms.ModelForm):
    firm = forms.CharField(label="",required=False)
    firm.widget.attrs.update({'placeholder': 'Firma (nieobowiązkowe)'})
    rodo=forms.BooleanField(label="RODO",required=True)
    class Meta:
        model=Profile
        fields=['firm','rodo']
