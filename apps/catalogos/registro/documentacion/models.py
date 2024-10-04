from django.db import models

# Create your models here.

from apps.catalogos.administracion.envio.models import Envio

class Documentacion(models.Model):
    lista_de_productos = models.TextField()  
    fecha = models.DateField()  
    tipo_de_documento = models.CharField(max_length=100)  
    formato = models.CharField(max_length=50)  
    envio = models.ForeignKey(Envio, verbose_name='Envio', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Documentaciones'

    def __str__(self):
        return f"Tipo de Documento: {self.tipo_de_documento}, Fecha: {self.fecha}"
