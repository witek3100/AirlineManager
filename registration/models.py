from django.contrib.auth.models import User
from django.db import models

class Airline(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(verbose_name='Airline name', max_length=200, null=True)
    budget = models.IntegerField(default=3000000)
    carried_passengers = models.IntegerField(default=0)
    completed_flights = models.IntegerField(default=0)
    def __str__(self):
        return self.name