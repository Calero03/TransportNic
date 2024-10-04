from django.db import models

# Create your models here.

class Ruta(models.Model):
    origen = models.CharField(max_length=255)  
    destino = models.CharField(max_length=255)  
    distancia = models.DecimalField(max_digits=10, decimal_places=2)  

    class Meta:
        verbose_name_plural = 'Rutas'

    def __str__(self):
        return f"Ruta: {self.origen} -> {self.destino}, Distancia: {self.distancia} km"
