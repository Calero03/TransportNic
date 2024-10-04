from django.db import models

# Create your models here.
from apps.catalogos.administracion.factura.models import Factura

class Envio(models.Model):
    id = models.AutoField(primary_key=True)  
    cantidad = models.IntegerField()  
    fecha_envio = models.DateField() 
    codigo_carga = models.CharField(max_length=50) 
    factura = models.ForeignKey(Factura, verbose_name='Factura', on_delete=models.PROTECT) 

    class Meta:
        verbose_name_plural = 'Envios'

    def __str__(self):
        return f"Envio ID: {self.id}, Cantidad: {self.cantidad}, Fecha: {self.fecha_envio}, Código: {self.codigo_carga}"
