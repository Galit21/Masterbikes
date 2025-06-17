from django.contrib import admin
from .models import Usuarios, Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'stock')
    search_fields = ('nombre', 'descripcion')
@admin.register(Usuarios)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'rut')
    search_fields = ('nombre', 'apellido', 'email', 'rut')
