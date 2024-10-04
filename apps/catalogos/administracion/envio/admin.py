from django.contrib import admin

# Register your models here.

from apps.catalogos.administracion.envio.models import Envio

@admin.register(Envio)
class EnvioAdmin(admin.ModelAdmin):
    search_fields = ['fecha_envio', 'codigo_carga']
    list_display = ['cantidad', 'fecha_envio', 'codigo_carga', 'factura']