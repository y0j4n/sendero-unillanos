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
    banner = models.ImageField(blank=True, null=True)
    titulo_seccion1 = models.CharField(max_length=500)
    img_seccion1 = models.ImageField(blank=True, null=True)
    parrafo1_seccion1 = models.CharField(max_length=2000)
    parrafo2_seccion1 = models.CharField(max_length=2000)
    titulo_seccion2 = models.CharField(max_length=500)
    img_seccion2 = models.ImageField(blank=True, null=True)
    parrafo1_seccion2 = models.CharField(max_length=2000)
    parrafo2_seccion2 = models.CharField(max_length=2000, blank=True, null=True)
    class Meta:
        verbose_name = 'Presentacion'
        verbose_name_plural = 'Presentacion'

    pass
