from django import forms
from main.models import Hub, Plane, Flight, Airport

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
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateFlightForm, self).__init__(*args, **kwargs)
        self.fields['plane_id'].choices = [(i, plane) for i, plane in enumerate(self.user.airline.plane_set.all()) if not hasattr(plane, 'flight')]
        self.fields['departure_airport'].choices = [(i, hub.airport_id) for i, hub in enumerate(self.user.airline.hub_set.all())]
class CreateFlightForAircraftForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['departure_airport', 'arrival_airport']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateFlightForAircraftForm, self).__init__(*args, **kwargs)
        print([(i, hub.airport_id) for i, hub in enumerate(self.user.airline.hub_set.all())])
        self.fields['departure_airport'].choices = ((i, hub.airport_id) for i, hub in enumerate(self.user.airline.hub_set.all()))