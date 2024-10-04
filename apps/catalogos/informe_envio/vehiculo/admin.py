from django.contrib import admin

# Register your models here.
from apps.catalogos.informe_envio.vehiculo.models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    search_fields = ['tipo_de_vehiculo', 'descripcion']
    list_display = ['tipo_de_vehiculo', 'capacidad', 'consumo', 'ruta']