from django.shortcuts import render

def main_page(response):
    return render(response, "registration/main.html", {})

def signup(response):
    '''TODO'''
    pass

def login(response):
    '''TODO'''
    pass