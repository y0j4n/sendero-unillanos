from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
from singleton_model import SingletonModel


class Contacto(SingletonModel):
    titulo = models.CharField(max_length=500)
    subtitulo1_seccion1 = models.CharField(max_length=500)
    parrafo1_seccion1 = models.CharField(max_length=500)
    subtitulo2_seccion1 = models.CharField(max_length=500)
    parrafo2_seccion1 = models.CharField(max_length=500)
    subtitulo_seccion2 = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contacto'

    pass
