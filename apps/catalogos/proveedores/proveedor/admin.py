from django.contrib import admin

# Register your models here.

from apps.catalogos.proveedores.proveedor.models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    search_fields = ['nombre_proveedor', 'descripcion']
    list_display = ['nombre_proveedor', 'direccion', 'telefono', 'email']