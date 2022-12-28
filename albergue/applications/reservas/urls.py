
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name='reservas_app'

urlpatterns = [
    path("listar_reservas/", login_required(views.listar), name='listar_reservas'),
    path("prueba/", login_required(views.prueba), name='prueba'),
    path("registro_reservas/", login_required(views.ReservaRegisterView.as_view()), name='registro_reservas'),
    
]