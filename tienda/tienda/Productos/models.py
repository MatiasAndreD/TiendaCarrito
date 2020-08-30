from django.db import models
from django.contrib.auth import get_user_model

class Producto(models.Model):
    nombre = models.CharField(max_length=300)
    descripcion = models.TextField(max_length=2000)
    precio = models.IntegerField()

    def __str__(self):
      return self.nombre
    
class Comentario(models.Model):
    comentario = models.TextField(max_length=500)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=300)
    producto = models.ForeignKey(Producto, related_name="producto_comentarios",on_delete=models.CASCADE)

    def __str__(self):
      return self.comentario


class ImagenProducto(models.Model):
    descripcion = models.TextField(max_length=1000)
    producto = models.ForeignKey(Producto, related_name="producto_imagen",on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_productos')


class CarritoCompras(models.Model):
    producto = models.ForeignKey(Producto, related_name="carrito_producto",on_delete=models.CASCADE)
    usuario = models.ForeignKey(get_user_model(),related_name="carrito_usuario" ,on_delete=models.CASCADE)
    precio = models.IntegerField()
    direccion = models.CharField( max_length=300)
    datos_payu = models.CharField( max_length=600)

    def __str__(self):
      return self.producto

