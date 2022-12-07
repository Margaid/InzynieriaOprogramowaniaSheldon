from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    pass
    '''
    firma = forms.CharField(help_text='Podaj firme')
    
    class Meta:
        model = User
        fields = ('username', 'firma', 'password1', 'password2', )
        '''