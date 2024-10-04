from django.contrib import admin

# Register your models here.

from apps.catalogos.administracion.carga.models import Carga

@admin.register(Carga)
class CargaAdmin(admin.ModelAdmin):
    search_fields = ['fecha_de_carga', 'destino', 'tipo_de_carga']
    list_display = ['fecha_de_carga', 'peso_de_carga', 'titulo', 'destino', 'tipo_de_carga','envio']
