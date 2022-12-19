from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Para internacionalización
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    
    GENERO_CHOICES=(
        ('M',_('Masculino')),
        ('F',_('Femenino')),
        ('O',_('Otro')),
    )
    
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    nombre = models.CharField(_('Nombre'),max_length=30, blank=True)
    primer_apellido = models.CharField(max_length=30, blank=True)
    segundo_apellido = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD='username'
    
    REQUIRED_FIELDS=['email',]
    
    objects=UserManager()
    
    class Meta:
        verbose_name=_('Usuario')
        verbose_name_plural=_('Usuarios')
    
    def __str__(self):
        return self.username
    