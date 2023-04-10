from django.contrib.auth.decorators import login_required
from main.forms import CreateHubForm, BuyAircraftForm, CreateFlightForm, CreateFlightForAircraftForm, DeleteFlightForm
from django.shortcuts import render, redirect
from main.models import Flight, Plane

@login_required
def home_page(request):
    flights = Flight.objects.filter(plane_id__airline_id__user=request.user)
    return render(request, 'main/home.html', {'flights' : flights})

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
            request.user.airline.budget -= request.user.airline.hub_set.count() * 500000
            request.user.airline.save()
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
        67378 :
            ('Boeing 737-800', 170, 5800, 1100000),
        98 :
            ('Bombardier Dash-8', 70, 2000, 200000),
        9700 :
            ('Bombardier CRJ-700', 80, 3500, 300000),
        43509 :
            ('Airbus A350-900', 350, 17000, 30000000)
    }
    if request.method =="POST":
        form_buy_aircraft = BuyAircraftForm(request.POST)
        if form_buy_aircraft.is_valid():
            aircraft = form_buy_aircraft.save(commit=False)
            aircraft.airline_id = request.user.airline
            aircraft.type = models_dict[modelid][0]
            aircraft.seats = models_dict[modelid][1]
            aircraft.range = models_dict[modelid][2]
            request.user.airline.budget -= models_dict[modelid][3]
            aircraft.save()
            request.user.airline.save()
            return redirect("/main/fleet")
    else:
        form_buy_aircraft = BuyAircraftForm()
    return render(request, "main/buy_aircraft.html", {'model' : models_dict[modelid][0], 'form' : form_buy_aircraft})

@login_required
def fleet(request):
    return render(request, "main/fleet.html")

@login_required
def flights(request):
    flights = Flight.objects.filter(plane_id__airline_id__user=request.user)
    return render(request, "main/flights.html", {'flights':flights})

@login_required
def create_flight(request):
    if request.method == "POST":
        create_flight_form = CreateFlightForm(request.POST, user=request.user)
        if create_flight_form.is_valid():
            create_flight_form.save()
            return redirect("/main/flights")
    else:
        create_flight_form = CreateFlightForm(user=request.user)
    return render(request, 'main/create_flight.html', {'form':create_flight_form})

@login_required
def create_flight_for_aircraft(request, aircraftid):
    aircraft = request.user.airline.plane_set.get(plane_id=aircraftid)
    if request.method == "POST":
        create_flight_form = CreateFlightForAircraftForm(request.POST, user=request.user)
        if create_flight_form.is_valid():
            flight = create_flight_form.save(commit=False)
            flight.plane_id = Plane.objects.get(plane_id=aircraftid)
            create_flight_form.save()
            return redirect("/main/fleet")
    else:
        create_flight_form = CreateFlightForAircraftForm(user=request.user)
    return render(request, 'main/create_flight_for_aircraft.html', {'form':create_flight_form, 'aircraft':aircraft})

@login_required
def delete_flight(request, flightid):
    flight = Flight.objects.get(flight_id=flightid)
    if request.method == "POST":
        delete_flight_form = DeleteFlightForm(request.POST)
        if delete_flight_form.is_valid():
            flight.delete()
            return redirect('/main/flights')
    return render(request, 'main/delete_flight.html', {'flight' : flight})

