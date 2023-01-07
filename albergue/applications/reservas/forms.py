from django import forms
from .models import Reserva
from django.http import JsonResponse
from django.db.models import Sum,Count
from django.utils.translation import gettext_lazy as _

class ReservaRegisterForm(forms.ModelForm):
    
   
    
    class Meta:
        
        model= Reserva
        fields=(
            'camas_reservadas',   
            'fecha_reserva_entrada',
            'documentos',
                )
        widgets={
            'fecha_reserva_entrada':forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={
                    'type':'date'
                }
                
            )
        }
    def clean(self):
        cleaned_data=super(ReservaRegisterForm,self).clean()
        camas_reservadas=self.cleaned_data['camas_reservadas']
        fecha_reserva_entrada=self.cleaned_data['fecha_reserva_entrada']
        # consulta=Reserva.objects.raw('SELECT num_reserva,fecha_reserva_entrada, SUM(camas_reservadas) as camas_reservadas  from reserva  where fecha_reserva_entrada="fecha_reserva_entrada" group by fecha_reserva_entrada')
        consulta=Reserva.objects.all().filter(fecha_reserva_entrada=self.cleaned_data['fecha_reserva_entrada']).aggregate(Sum('camas_reservadas'))
        for con in consulta:
           if consulta[con]!=None:
                camas_disponibles=7-consulta[con]
                if camas_disponibles==0:
                    error=_("No hay camas disponibles para el día ")+str(fecha_reserva_entrada)
                    raise forms.ValidationError(error)
                if consulta[con]+camas_reservadas>7:
                    error=_("El número de camas disponibles para el día ")+str(fecha_reserva_entrada)+ " es de " +str(camas_disponibles)
                    raise forms.ValidationError(error)
                
        # self.add_error('camas_reservadas',error)
        print (camas_reservadas)
        print (fecha_reserva_entrada)
            