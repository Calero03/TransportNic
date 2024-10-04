from django.contrib import admin

# Register your models here.
from apps.catalogos.detalle_carga.producto.models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'descripcion']
    list_display = ['nombre', 'descripcion', 'peso_kg', 'precio', 'carga']
