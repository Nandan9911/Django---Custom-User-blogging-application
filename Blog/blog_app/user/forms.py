from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person


class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()
    country = forms.CharField()

    class Meta:
        model = Person
        fields = ['first_name','last_name','email','city','country','username','password1', 'password2']

