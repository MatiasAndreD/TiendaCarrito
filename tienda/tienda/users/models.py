from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for Tienda."""

    #: First and last name do not cover name patterns around the globe
    telefono = CharField(_("Telefono"), blank=True, max_length=9)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sexos = (
        ('F', 'Femenino',),
        ('M', 'Masculino',),
        ('U', 'No especificar',),
    )
    sex = models.CharField(
        max_length=1,
        choices=sexos,
    )
    