from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="homepage"),
    path('hubs', views.hubs_page, name="hubspage"),
    path('create_hub', views.create_hub, name="createhub"),
    path('aircraftmarket', views.aircraft_market, name="circraftmarket"),
    path('buy/<int:modelid>', views.buy_aircraft, name='buyaircraft'),
    path('fleet', views.fleet, name="fleet"),
    path('flights', views.flights, name="flights"),
    path('createflight', views.create_flight, name="createflight")
]