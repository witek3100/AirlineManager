from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="registration/main.html"), name="mainpage"),
    path('signup/', views.signup, name="signup"),
    path('accountcreated/', TemplateView.as_view(template_name="registration/account_created.html"), name="accountcreated"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

]