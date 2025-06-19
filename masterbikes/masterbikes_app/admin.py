from django.contrib import admin
from .models import Usuario, Producto, Categoria

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'stock')
    search_fields = ('nombre', 'descripcion', 'precio', 'stock')
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria','nombre')
    search_fields = ('id_categoria','nombre')
@admin.register(Usuario)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'rut')
    search_fields = ('nombre', 'apellido', 'email', 'rut')
