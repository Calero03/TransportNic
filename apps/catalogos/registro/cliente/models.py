from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Cliente'

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}" 


