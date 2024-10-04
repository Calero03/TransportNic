from django.db import models
# Create your models here.
from apps.catalogos.registro.cliente.models import Cliente

class Factura(models.Model):
    numero_factura = models.CharField(max_length=50, primary_key=True)
    fecha_emision = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.PROTECT) 

    class Meta:
        verbose_name_plural = 'Factura'

    def __str__(self):
        return f"Factura: {self.numero_factura}, Cliente: {self.cliente}, Total: {self.total}"
