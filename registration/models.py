from django.db import models
from django.contrib.auth.models import User

class Airline(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    airline_id = models.AutoField(verbose_name='airline name', primary_key=True)
    name = models.CharField(max_length=20)
    budget = models.IntegerField()
