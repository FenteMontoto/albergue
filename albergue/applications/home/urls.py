
from django.urls import path

from . import views

app_name='home_app'

urlpatterns = [
    path("index/", views.HomePage.as_view(), name='index'),
    path("reservas/", views.Reservas.as_view(), name='reservas'),
]
