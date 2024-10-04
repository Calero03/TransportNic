from django.db import models

# Create your models here.

from apps.catalogos.administracion.carga.models import Carga

class Producto(models.Model):
    nombre = models.CharField(max_length=255)  
    descripcion = models.TextField(blank=True, null=True)  
    peso_kg = models.DecimalField(max_digits=10, decimal_places=2)  
    precio = models.DecimalField(max_digits=10, decimal_places=2)  
    carga = models.ForeignKey(Carga, verbose_name='Carga', on_delete=models.PROTECT, default=1) 

    class Meta:
        verbose_name_plural = 'Producto'

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}"
