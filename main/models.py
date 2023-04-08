from django.db import models
from django.contrib.auth.models import User

class Airline(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="airlineuser")
    airline_id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='airline name', max_length=20)
    budget = models.IntegerField()

class Plane(models.Model):
    plane_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    airline_id = models.ForeignKey(Airline, on_delete=models.CASCADE)
    seats = models.IntegerField()

class Airport(models.Model):
    airport_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=20)
    code = models.CharField(max_length=4)
    popularity = models.IntegerField()
    longtitude = models.IntegerField()
    latitude = models.IntegerField()

class Hub(models.Model):
    hub_id = models.AutoField(primary_key=True)
    airline_id = models.ForeignKey(Airline, on_delete=models.CASCADE)
    airport_id = models.ForeignKey(Airport, on_delete=models.CASCADE)

class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    airline_id = models.ForeignKey(Airline, on_delete=models.CASCADE)
    plane_id = models.ForeignKey(Plane, on_delete=models.CASCADE)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departure")
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrival")