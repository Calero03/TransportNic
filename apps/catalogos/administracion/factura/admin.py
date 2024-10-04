from django.contrib import admin

# Register your models here.
from apps.catalogos.administracion.factura.models import Factura

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    search_fields = ['numero_factura', 'fecha_emision']
    list_display = ['numero_factura', 'fecha_emision', 'total', 'cliente']
