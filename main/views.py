from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home_page(response):
    return render(response, 'main/home.html')