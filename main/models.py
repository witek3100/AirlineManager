from django.db import models
from registration.models import Airline

class Plane(models.Model):
    plane_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    airline_id = models.ForeignKey('registration.Airline', on_delete=models.CASCADE)
    seats = models.IntegerField()
    range = models.IntegerField()
    registration = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.registration} {self.type}'

class Airport(models.Model):
    airport_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=20)
    code = models.CharField(max_length=4)
    popularity = models.IntegerField()
    longtitude = models.IntegerField(default=0)
    latitude = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.city} {self.code}'

class Hub(models.Model):
    hub_id = models.AutoField(primary_key=True)
    airline_id = models.ForeignKey('registration.Airline', on_delete=models.CASCADE)
    airport_id = models.ForeignKey(Airport, verbose_name="airport", on_delete=models.CASCADE)

class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    plane_id = models.OneToOneField(Plane, verbose_name='Aircraft', on_delete=models.CASCADE)
    departure_airport = models.ForeignKey(Airport, verbose_name='Departure airport', on_delete=models.CASCADE, related_name="departure")
    arrival_airport = models.ForeignKey(Airport, verbose_name='Arrival airport', on_delete=models.CASCADE, related_name="arrival")
    arrival_time = models.DateTimeField(null=True)
