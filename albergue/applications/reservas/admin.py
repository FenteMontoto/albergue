from django.contrib import admin

from .models import Reserva, User


class ReservaAdmin(admin.ModelAdmin):
     list_display=('nombre_usuario','camas_reservadas','fecha_reserva_entrada','pago_confirmado',
            'documentos',)

admin.site.register(Reserva,ReservaAdmin)

