from django.shortcuts import render, redirect
from registration.forms import CreateUserForm, CreateAirlineForm
def main_page(response):
    return render(response, "registration/main.html")

def signup(request):
    if request.method == "POST":
        form_user = CreateUserForm(request.POST)
        form_airline = CreateAirlineForm(request.POST)
        if form_user.is_valid() and form_airline.is_valid():
            user = form_user.save()
            airline = form_airline.save(commit=False)
            airline.user = user
            airline.budget = 3000000
            airline.save()
            return redirect("/accountcreated")
    else:
        form_user = CreateUserForm()
        form_airline = CreateAirlineForm()
    return render(request, "registration/signup.html", {"formuser" : form_user, "formairline" : form_airline})

def login(request):
    return render(request, "registration/login.html")

def account_created(request):
    return render(request, "registration/account_created.html")