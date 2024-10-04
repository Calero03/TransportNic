from django.contrib import admin

# Register your models here.

from apps.catalogos.registro.documentacion.models import Documentacion

@admin.register(Documentacion)
class DocumentacionAdmin(admin.ModelAdmin):
    search_fields = ['lista_de_productos', 'fecha']
    list_display = ['lista_de_productos', 'fecha', 'tipo_de_documento', 'formato']