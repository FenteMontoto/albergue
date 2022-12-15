from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    
    GENERO_CHOICES=(
        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otro'),
    )
    
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    nombre = models.CharField(max_length=30, blank=True)
    primer_apellido = models.CharField(max_length=30, blank=True)
    segundo_apellido = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD='username'
    
    REQUIRED_FIELDS=['email',]
    
    objects=UserManager()
    
    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
    
    def __str__(self):
        return self.username
    