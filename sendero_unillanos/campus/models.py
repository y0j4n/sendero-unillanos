from django.db import models

# Create your models here.
from singleton_model import SingletonModel


class Campus(SingletonModel):
    titulo = models.CharField(max_length=100)
    banner = models.ImageField()
    titulo_seccion1 = models.CharField(max_length=250)
    parrafo_seccion1 = models.CharField(max_length=250)
    img_seccion1 = models.ImageField(blank=True, null=True)
    titulo_seccion2 = models.CharField(max_length=250, blank=True, null=True)
    parrafo_seccion2 = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campus'

    pass
