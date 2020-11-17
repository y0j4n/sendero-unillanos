from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
from singleton_model import SingletonModel


class Educacion(SingletonModel):
    titulo_seccion1 = models.CharField(max_length=500)
    parrafo_seccion1 = models.CharField(max_length=500)
    img_seccion1 = models.ImageField()
    titulo_seccion2 = models.CharField(max_length=500)
    parrafo_seccion2 = models.CharField(max_length=500)
    img_seccion2 = models.ImageField()
    titulo_seccion3 = models.CharField(max_length=500)
    parrafo_seccion3 = models.CharField(max_length=500)
    img_seccion3 = models.ImageField()
    parrafo2_seccion3 = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Educacion'
        verbose_name_plural = 'Educacion'

    pass
