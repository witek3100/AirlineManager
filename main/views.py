from django.contrib.auth.decorators import login_required
from main.forms import CreateHubForm
from django.shortcuts import render, redirect

@login_required
def home_page(response):
    return render(response, 'main/home.html')

@login_required
def hubs_page(request):
    return render(request, 'main/hubs.html')

@login_required
def create_hub(request):
    if request.method == "POST":
        form_hub = CreateHubForm(request.POST)
        if form_hub.is_valid():
            hub = form_hub.save(commit=False)
            hub.airline_id = request.user.airline
            hub.save()
            return redirect("/main/hubs")
    else:
        form_hub = CreateHubForm()
    return render(request, "main/create_hub.html", {"formhub" : form_hub})

@login_required
def aircraft_market(request):
    return render(request, "main/aircraft_market.html")

@login_required
def buy_aircraft(request, modelid):
    models_dict = {
        '67378' :
            ('Boeing 737-800', 170, 5800, 1100000)
    }
    return render(request, "main/buy_aircraft.html", {'model' : models_dict[modelid]})