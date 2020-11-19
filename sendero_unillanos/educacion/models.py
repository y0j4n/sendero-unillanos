from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
from singleton_model import SingletonModel


class Educacion(SingletonModel):
    img1_seccion1 = models.ImageField(null=True, blank=True)
    img2_seccion1 = models.ImageField(null=True, blank=True)
    img3_seccion1 = models.ImageField(null=True, blank=True)
    titulo_seccion1 = models.CharField(max_length=500)
    parrafo_seccion1 = models.CharField(max_length=2000)
    titulo_seccion2 = models.CharField(max_length=500)
    parrafo1_seccion2 = models.CharField(max_length=2000)
    parrafo2_seccion2 = models.CharField(max_length=2000)
    img_seccion2 = models.ImageField()
    titulo_seccion3 = models.CharField(max_length=500)
    parrafo_seccion3 = models.CharField(max_length=2000)
    img_seccion3 = models.ImageField()
    parrafo2_seccion3 = models.CharField(max_length=500)
    banner = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = 'Educacion'
        verbose_name_plural = 'Educacion'

    pass
