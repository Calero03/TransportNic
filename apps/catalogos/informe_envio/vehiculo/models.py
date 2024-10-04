from django.db import models

# Create your models here.

from apps.catalogos.informe_envio.ruta.models import Ruta

class Vehiculo(models.Model):
    tipo_de_vehiculo = models.CharField(max_length=100)  
    capacidad = models.DecimalField(max_digits=10, decimal_places=2)  
    consumo = models.DecimalField(max_digits=10, decimal_places=2)  
    ruta = models.ForeignKey(Ruta, verbose_name='Ruta', on_delete=models.PROTECT) 

    class Meta:
        verbose_name_plural = 'Vehículos'

    def __str__(self):
        return f"Vehículo: {self.tipo_de_vehiculo}, Capacidad: {self.capacidad}, Consumo: {self.consumo}"
