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
from django.db.models import Sum,Count

# class ListarReservasView(ListView):
#     model=Reserva
#     template_name='reservas/listar_reservas.html'
#     # queryset=Reserva.objects.aggregate(reservas=Sum('camas_reservadas'))
#     # # context_object_name='queryset'
#     context_object_name='lista_prueba'  
   
   
    
class ReservaRegisterView(CreateView):
   
    template_name='reservas/registro_reservas.html'
    form_class=ReservaRegisterForm 
    success_url="/"
    
   
def listar(request):
    return render(request,'reservas/listar_reservas.html')
   
   
      
    
    