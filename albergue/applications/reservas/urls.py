
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name='reservas_app'

urlpatterns = [
    path("listar_reservas/", login_required(views.ListarReservasView.as_view()), name='listar_reservas'),
    path("registro_reservas/", login_required(views.ReservaRegisterView.as_view()), name='registro_reservas'),
    
]