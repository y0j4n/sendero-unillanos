from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from singleton_model import SingletonModel


class Contacto(SingletonModel):
    titulo = models.CharField(max_length=500)
    banner = models.ImageField(blank=True, null=True)
    subtitulo1 = models.CharField(max_length=500)
    parrafo1 = models.CharField(max_length=500)
    subtitulo2 = models.CharField(max_length=500)
    direccion = models.CharField(max_length=500)
    telefono = models.PositiveIntegerField()
    email = models.EmailField()
    Otro = models.CharField(max_length=100, blank=True, null=True)
    subtitulo3 = models.CharField(max_length=500)
    Enlace1 = models.CharField(max_length=300, blank=True, null=True)
    Enlace2 = models.CharField(max_length=300, blank=True, null=True)
    Enlace3 = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contacto'

    pass
