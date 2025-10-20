from django.contrib import admin
from .models import Cliente, Producto, Tienda

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'fecha_registro')  # columnas visibles
    search_fields = ('nombre', 'apellido', 'email')  # barra de búsqueda
    list_filter = ('fecha_registro',)  # filtro lateral

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria')  
    search_fields = ('nombre', 'categoria')
    list_filter = ('categoria',)

@admin.register(Tienda)
class TiendaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'zona')
    search_fields = ('nombre', 'zona')
    list_filter = ('zona',)

