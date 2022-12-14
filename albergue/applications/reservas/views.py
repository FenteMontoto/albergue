from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse_lazy, reverse
# from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _


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
from django.http import JsonResponse
from applications.reservas.models import Reserva


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
    all_events = Reserva.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'reservas/listar_reservas.html',context)
   

    
# def all_events(request):                                                                                                 
#     all_events = Reserva.objects.raw('SELECT num_reserva,fecha_reserva_entrada, (7-SUM(camas_reservadas))as camas_reservadas  from reservas_reserva group by fecha_reserva_entrada')
#     # print(all_events)
#     camas=0    
#     out=[]                                                                                                        
#     for event in all_events:                                                                                             
                                                                                                     
#         out.append({    
#             'title': event.camas_reservadas,                                                                                                                                                                              
#             'start': event.fecha_reserva_entrada,                                                                                                                     
#         })                                                                                                               
                                                                                                                      
#     return JsonResponse(out, safe=False) 

def prueba(request):  
    all_events = Reserva.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'reservas/prueba.html',context)
 
def all_events(request):                                                                                                 
    # all_events = Reserva.objects.raw('SELECT num_reserva,fecha_reserva_entrada, (7-SUM(camas_reservadas))as camas_reservadas  from reserva group by fecha_reserva_entrada')     
    all_events = Reserva.objects.raw('SELECT num_reserva,fecha_reserva_entrada, SUM(camas_reservadas) as camas_reservadas  from reserva group by fecha_reserva_entrada')                                                                                   
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': (str(event.camas_reservadas)+_(" camas reservadas")),                                                                                         
            'id': event.camas_disponibles,                                                                                              
            'start': event.fecha_reserva_entrada,                                                       
            # 'end': event.fecha_reserva_entrada.strftime("%m/%d/%Y"),                                                         
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False)