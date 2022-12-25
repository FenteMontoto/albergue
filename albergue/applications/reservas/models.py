import os
from django.db import models
from django.utils.translation import gettext_lazy as _
from applications.users.models import User


class Reserva(models.Model):
    
    num_reserva = models.AutoField(_('Reserva nº'),primary_key=True)
    nombre_usuario=models.ForeignKey(User,related_name='+',blank=True,null=True,on_delete=models.CASCADE)
    mail_usuario=models.ForeignKey(User,related_name='+',blank=True,null=True,on_delete=models.CASCADE)
    camas_reservadas = models.IntegerField(_('Nº de camas reservadas'),default=1)
    fecha_reserva_entrada = models.DateField(_('Fecha de entrada'), auto_now=False, auto_now_add=False,blank=True,null=True)
    pago_confirmado = models.BooleanField(_('Pago confirmado'),default=False)
    documentos = models.ImageField(_('Documentación'), upload_to='media/', height_field=None, width_field=None, max_length=None,blank=True,null=True)
    camas_disponibles = models.IntegerField(_('Camas disponibles'),default=7,blank=True,null=True,editable=False)
    
   
    class Meta:
        verbose_name=_('Reserva')
        verbose_name_plural=_('Reservas')
        ordering=['num_reserva']
    
    REQUIRED_FIELDS=['camas_reservadas','fecha_reserva_entrada','documentos']
    # def __str__(self):
    #     return str(self.documentos)
    
    def save(self,*args,**kwargs):
        self.fecha_reserva_entrada=self.fecha_reserva_entrada
        super().save(*args,*kwargs)