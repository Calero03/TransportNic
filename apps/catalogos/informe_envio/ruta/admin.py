from django.contrib import admin

from apps.catalogos.informe_envio.ruta.models import Ruta


@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    search_fields = ['origen', 'destino']
    list_display = ['origen', 'destino', 'distancia']