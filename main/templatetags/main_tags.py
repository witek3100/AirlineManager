import math
from django import template
import geopy.distance

register = template.Library()

@register.filter(name='mul')
def mul(value, arg):
    return value * arg

@register.filter(name='distance')
def distance(flight):
    coords_1 = (flight.departure_airport.latitude, flight.departure_airport.longtitude)
    coords_2 = (flight.arrival_airport.latitude, flight.arrival_airport.longtitude)
    return int(geopy.distance.geodesic(coords_1, coords_2).km)

@register.filter(name='income')
def income(flight):
    return int(flight.plane_id.seats * distance(flight) * flight.arrival_airport.popularity * 0.0005) + 10000

@register.filter(name='gettime')
def gettime(time):
    return time.strftime("%H:%M %p")