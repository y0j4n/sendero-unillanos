from django.db import models

# Create your models here.
from singleton_model import SingletonModel


class Campus(SingletonModel):
    titulo = models.CharField(max_length=100)
    banner = models.ImageField()
    subtitulo_seccion1 = models.CharField(max_length=250)
    parrafo1_seccion1 = models.CharField(max_length=250, null=True, blank=True)
    subtitulo_seccion2 = models.CharField(max_length=250)
    parrafo1_seccion2 = models.CharField(max_length=250, null=True, blank=True)
    parrafo2_seccion2 = models.CharField(max_length=250, null=True, blank=True)
    parrafo3_seccion2 = models.CharField(max_length=250, null=True, blank=True)
    subtitulo_seccion3 = models.CharField(max_length=250)
    parrafo1_seccion3 = models.CharField(max_length=250, null=True, blank=True)
    parrafo2_seccion3 = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campus'

    pass
