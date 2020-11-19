from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from singleton_model import SingletonModel


class Presentacion(SingletonModel):
    titulo_de_la_pagina = models.CharField(max_length=50)
    icono_de_la_pagina = models.ImageField(blank=True, null=True)
    logo_de_la_pagina = models.ImageField(blank=True, null=True)
    titulo_seccion1 = models.CharField(max_length=500)
    parrafo_seccion1 = models.CharField(max_length=500)
    img_seccion1 = models.ImageField(blank=True, null=True)
    titulo_seccion2 = models.CharField(max_length=500)
    parrafo_seccion2 = models.CharField(max_length=500)
    img_seccion2 = models.ImageField(blank=True, null=True)
    banner = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = 'Presentacion'
        verbose_name_plural = 'Presentacion'

    pass
