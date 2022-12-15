from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect

from django.views.generic import(
    View,
    CreateView
)
from django.views.generic.edit import(
    FormView
)
from .forms import UserRegisterForm, LoginForm

from .models import User

class UserRegisterView(FormView):
    template_name='users/registro.html'
    form_class=UserRegisterForm 
    success_url='/'
    
    def form_valid(self, form):
        
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombre=form.cleaned_data['nombre'],
            primer_apellido=form.cleaned_data['primer_apellido'],
            segundo_apellido=form.cleaned_data['segundo_apellido'],
            genero=form.cleaned_data['genero'],
        )
        return super(UserRegisterView,self).form_valid(form)
    
class Login(FormView):
    template_name='users/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('home_app:index')
    
    def form_valid(self, form):
        user=authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(Login, self).form_valid(form)
    

class Logout(View):
    
    def get(self,request, *args,**kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'home_app:index'
            )
        )