from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="homepage"),
    path('hubs', views.hubs_page, name="hubspage")
]