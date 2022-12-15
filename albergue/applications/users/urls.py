
from django.urls import path

from . import views

app_name='users_app'

urlpatterns = [
    path("registro/", views.UserRegisterView.as_view(), name='registro'),
    path("login/", views.Login.as_view(), name='login'),
]
