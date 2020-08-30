from django.contrib import admin
from .models import Producto, Comentario, ImagenProducto, CarritoCompras
# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
   list_display = ('nombre', 'precio')


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario','producto','comentario')


@admin.register(ImagenProducto)
class ImagenAdmin(admin.ModelAdmin):
   list_display = ('producto', 'descripcion')

@admin.register(CarritoCompras)
class Carrito(admin.ModelAdmin):
    pass