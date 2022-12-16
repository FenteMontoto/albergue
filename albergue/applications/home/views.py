from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse_lazy,reverse

from django.views.generic import(
    TemplateView
)

class HomePage(TemplateView):
    template_name="home/index.html"
    
    
class Reservas(LoginRequiredMixin,TemplateView):
    template_name="home/reservas.html"
    login_url=reverse_lazy('users_app:login')
    
