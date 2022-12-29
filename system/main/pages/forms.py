from django import forms
from register.models import Profile

#formularz potrzebny do zmian dokonanych przez admina przy zatwierdzaniu użytkownika
class ProfileForm_for_admin(forms.ModelForm):
    is_user=forms.BooleanField()
    is_operator=forms.BooleanField()
    is_admin=forms.BooleanField()
    firm = forms.CharField(max_length=100)
    #operatorzy i lista
    class Meta:
        model=Profile
        fields=['is_user','is_operator','is_admin','firm']
