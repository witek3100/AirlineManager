from django import forms
from main.models import Hub, Plane

class CreateHubForm(forms.ModelForm):
    class Meta:
        model = Hub
        fields = ["airport_id"]

class BuyAircraft(forms.ModelForm):
    class Meta:
        model = Plane