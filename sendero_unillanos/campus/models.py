from django.db import models

# Create your models here.
from singleton_model import SingletonModel


class Campus(SingletonModel):
    titulo_seccion1 = models.CharField(max_length=250)
    parrafo_seccion1 = models.CharField(max_length=250)
    img_seccion1 = models.ImageField()
    titulo_seccion2 = models.CharField(max_length=250)
    parrafo_seccion2 = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campus'

    pass
