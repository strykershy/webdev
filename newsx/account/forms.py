from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from dobwidget import DateOfBirthWidget



class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Insert a valid email address.')
    dob = forms.DateField(widget=DateOfBirthWidget)
    

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'dob',
            'email',
            'password1',
            'password2',
            )
    
    