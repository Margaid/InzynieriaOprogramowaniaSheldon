from django import forms
from register.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


#formularz potrzebny do zmian dokonanych przez admina przy zatwierdzaniu użytkownika
class ProfileForm_for_admin(forms.ModelForm):
    is_user=forms.BooleanField(required=False)
    is_operator=forms.BooleanField(required=False,)
    is_admin=forms.BooleanField(required=False)
    firm = forms.CharField(max_length=100,required=False,label="")
    #operatorzy i lista

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
       # self.helper.form_tag=False
        self.helper.form_id="form_id"
        self.helper.layout = Layout(
            'is_user',
            'is_operator',
            'is_admin',
            'firm',
            
            Submit('submit', 'zatwierdź',css_id="approving_button")
        )
    class Meta:
        model=Profile
        fields=['is_user','is_operator','is_admin','firm']
