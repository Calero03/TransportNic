from django.contrib import admin
# Register your models here.
from apps.catalogos.registro.cliente.models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ['nombre', 'direccion', 'telefono']

