from django import forms
from .models import Reserva

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