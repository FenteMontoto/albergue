from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect

from django.views.generic import(
    TemplateView
)

class HomePage(TemplateView):
    template_name="home/index.html"
    

