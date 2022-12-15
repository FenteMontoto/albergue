from django import forms 
from django.contrib.auth import authenticate

from .models import User

class UserRegisterForm(forms.ModelForm):
    
    password1=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )
    password2=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )
    
    class Meta:
        
        model=User
        fields=(
            'username',
            'email',
            'nombre',
            'primer_apellido',
            'segundo_apellido',
            'genero'
            )
        
    def clean_password2(self):
        if self.cleaned_data['password1']!=self.cleaned_data['password2']:
            self.add_error('password2','Las contraseñas introducidas no son iguales')
            
            
class LoginForm(forms.Form):
    username=forms.CharField(
        label='Usuario',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Usuario',
            }
        )
    )
    password=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )
    
    def clean(self):
        
        cleaned_data=super(LoginForm,self).clean()
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('El usuario o contraseña no son correctos')
        
        return self.cleaned_data
        