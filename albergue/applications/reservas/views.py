from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse_lazy, reverse
# from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect


from django.views.generic import(
    View,
    CreateView,
    ListView
)
from django.views.generic.edit import(
    FormView
)


from .models import Reserva

from .forms import ReservaRegisterForm

class ListarReservasView(ListView):
    template_name='reservas/listar_reservas.html'
    queryset=['a']
   
    
class ReservaRegisterView(CreateView):
   
    template_name='reservas/registro_reservas.html'
    form_class=ReservaRegisterForm 
    success_url="/"
    
   

    
   
   
      
    
    