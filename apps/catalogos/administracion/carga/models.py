from django.db import models

# Create your models here.

from apps.catalogos.administracion.envio.models import Envio

class Carga(models.Model):
    fecha_de_carga = models.DateField()
    peso_de_carga = models.DecimalField(max_digits=10, decimal_places=2)
    titulo = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    tipo_de_carga = models.CharField(max_length=100)
    envio = models.ForeignKey(Envio, verbose_name='Envio', on_delete=models.PROTECT) 

    class Meta:
        verbose_name_plural = 'Cargas'

    def __str__(self):
        return f"{self.titulo} - {self.tipo_de_carga}, kg: {self.peso_de_carga}"
