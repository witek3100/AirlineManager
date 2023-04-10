from django import forms
from main.models import Hub, Plane, Flight

class CreateHubForm(forms.ModelForm):
    class Meta:
        model = Hub
        fields = ["airport_id"]

class BuyAircraftForm(forms.ModelForm):
    class Meta:
        model = Plane
        fields = ['registration']

class CreateFlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['plane_id', 'departure_airport', 'arrival_airport']