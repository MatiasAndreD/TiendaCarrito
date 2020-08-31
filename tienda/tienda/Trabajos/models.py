from django.db import models

class Trabajo(models.Model):
    idTrabajo = models.AutoField(primary_key=True, null=False, blank=False, editable=False)
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to="ImagenesTrabajo")

    class Meta:
        verbose_name='trabajo'
        verbose_name_plural = 'trabajos'


    def __str__(self):
        return (self.nombre)