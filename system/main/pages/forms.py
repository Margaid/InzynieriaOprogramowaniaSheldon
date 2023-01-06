from django import forms
from register.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div,Row

OPERATORS=(
        ('','-----'),
        ('operator1','operator maszyny 1'),
        ('operator2','operator maszyny 2'),
        )

#formularz potrzebny do zmian dokonanych przez admina przy zatwierdzaniu użytkownika
class ProfileForm_for_admin(forms.ModelForm):
    is_user=forms.BooleanField(required=False,label="użytkownik")
    is_operator=forms.BooleanField(required=False,label="operator")
    is_admin=forms.BooleanField(required=False,label="admin")
    operator=forms.ChoiceField(choices=OPERATORS,required=False,label='jaki operator',
              #  widget=forms.CheckboxSelectMultiple
              )
    #operatorzy i lista

    #crispy form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id="form_id"
        self.helper.layout = Layout(
            'is_user',
            'is_admin',
            'is_operator',
            'firm',
            'operator',
            Submit('submit', 'Akceptuj',css_id="approving_button"),
            Submit('submit', 'Odrzuć',css_id="disapproving_button"),
            
        )
    class Meta:
        model=Profile
        fields=['is_user','is_operator','is_admin','operator']
