from django import forms
from register.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Row
from .models import LAB_STATIONS
from .models import ReservationDataBase
from datetime import date

OPERATORS = (
    ('', '-----'),
    ('operator1', 'operator maszyny 1'),
    ('operator2', 'operator maszyny 2'),
)

# formularz potrzebny do zmian dokonanych przez admina przy zatwierdzaniu użytkownika


class ProfileForm_for_admin(forms.ModelForm):
    is_user = forms.BooleanField(required=False, label="użytkownik")
    is_operator = forms.BooleanField(required=False, label="operator")
    is_admin = forms.BooleanField(required=False, label="admin")
    operator = forms.ChoiceField(choices=OPERATORS, required=False, label='Operator',
                                 #  widget=forms.CheckboxSelectMultiple
                                 )
    # operatorzy i lista

    # crispy form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "form_id"
        self.helper.layout = Layout(
            'is_user',
            'is_admin',
            'is_operator',
            'firm',
            'operator',
            Submit('submit', 'Odrzuć', css_id="disapproving_button"),

        )

    class Meta:
        model = Profile
        fields = ['is_user', 'is_operator', 'is_admin', 'firm', 'operator']


class ReservationForm_for_user(forms.ModelForm):
    operator = forms.ChoiceField(choices=OPERATORS, required=False, label='Operator',
                                 #  widget=forms.CheckboxSelectMultiple
                                 )
    lab_station = forms.ChoiceField(
        choices=LAB_STATIONS, required=False, label='Sala')
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if end_date <= start_date:
                raise forms.ValidationError(
                    "End date should be later than start date.")
            if start_date < date.today():
                raise forms.ValidationError(
                    "Start date should be later than or equal to today.")

    class Meta:
        model = ReservationDataBase
        fields = ['lab_station',
                  'start_date', 'end_date', 'operator']


class ReservationForm_for_operator(forms.ModelForm):
    lab_station = forms.ChoiceField(
        choices=LAB_STATIONS, required=False, label='Sala')
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if end_date <= start_date:
                raise forms.ValidationError(
                    "End date should be later than start date.")
            if start_date < date.today():
                raise forms.ValidationError(
                    "Start date should be later than or equal to today.")

    class Meta:
        model = ReservationDataBase
        fields = ['lab_station',
                  'start_date', 'end_date']


class ProfileForm_for_super_admin(forms.ModelForm):
    is_user = forms.BooleanField(required=False, label="użytkownik")
    is_operator = forms.BooleanField(required=False, label="operator")
    is_admin = forms.BooleanField(required=False, label="admin")
    operator = forms.ChoiceField(choices=OPERATORS, required=False, label='Operator',
                                 #  widget=forms.CheckboxSelectMultiple
                                 )
    # operatorzy i lista

    # crispy form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "form_id"
        self.helper.layout = Layout(
            'is_user',
            'is_admin',
            'is_operator',
            'operator',
            'firm',
            Submit('submit', 'Odrzuć', css_id="disapproving_button"),
            Submit('submit', 'Akceptuj', css_id="approving_button"),
        )

    class Meta:
        model = Profile
        fields = ['is_user', 'is_operator', 'is_admin', 'firm', 'operator']


class Form_for_approval_buttons_reservations_superadmin(forms.ModelForm):
    reservation_id = forms.IntegerField()
    # crispy form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "form_id_reservation"
        self.helper.layout = Layout(
            # 'reservation_id',
            Submit('submit', 'Odrzuć', css_id="disapproving_button_reservation"),
            Submit('submit', 'Akceptuj', css_id="approving_button_reservation"),
        )

    class Meta:
        model = ReservationDataBase
        fields = ['reservation_id', ]

        
class Form_for_approval_buttons_reservations_admin(forms.ModelForm):
    reservation_id = forms.IntegerField()
    # crispy form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "form_id_reservation"
        self.helper.layout = Layout(
            # 'reservation_id',
            Submit('submit', 'Odrzuć', css_id="disapproving_button_reservation"),
        )

    class Meta:
        model = ReservationDataBase
        fields = ['reservation_id', ]

