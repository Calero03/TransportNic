from django.db import models

# Create your models here.


class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=255, primary_key=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    

    class Meta:
        verbose_name_plural = 'Proveedore'

    def __str__(self):
        return f"Proveedor: {self.nombre_proveedor}, Email: {self.email}"
