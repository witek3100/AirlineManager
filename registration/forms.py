from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from main.models import Airline

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class CreateAirlineForm(forms.ModelForm):

    class Meta:
        model = Airline
        fields = ["name"]