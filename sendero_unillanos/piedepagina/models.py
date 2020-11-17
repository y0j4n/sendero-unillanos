from django.db import models


# Create your models here.
from singleton_model import SingletonModel


class Piedepagina(SingletonModel):
    subtitulo1 = models.CharField(max_length=250)
    parrafo1 = models.CharField(max_length=250)
    subtitulo2 = models.CharField(max_length=250)
    parrafo2 = models.CharField(max_length=250)
    subtitulo3 = models.CharField(max_length=250)
    parrafo3 = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Piedepagina'
        verbose_name_plural = 'Piedepagina'

    pass