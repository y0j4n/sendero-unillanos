from django.db import models

# Create your models here.
from singleton_model import SingletonModel


class Sendero(SingletonModel):
    titulo = models.CharField(max_length=500)
    banner = models.ImageField(null=True, blank=True)
    subtitulo_seccion1 = models.CharField(max_length=500)
    parrafo_seccion1 = models.CharField(max_length=500)
    img_seccion1 = models.ImageField()
    subtitulo_seccion2 = models.CharField(max_length=500)
    parrafo_seccion2 = models.CharField(max_length=500)
    img_seccion2 = models.ImageField()
    subtitulo_seccion3 = models.CharField(max_length=500)
    parrafo_seccion3 = models.CharField(max_length=500)
    img_seccion3 = models.ImageField()
    subtitulo_seccion4 = models.CharField(max_length=500)
    parrafo_seccion4 = models.CharField(max_length=500)
    img_seccion4 = models.ImageField()
    subtitulo_seccion5 = models.CharField(max_length=500)
    parrafo_seccion5 = models.CharField(max_length=500)
    img_seccion5 = models.ImageField()
    subtitulo_seccion6 = models.CharField(max_length=500)
    parrafo_seccion6 = models.CharField(max_length=500)
    img_seccion6 = models.ImageField()
    subtitulo_seccion7 = models.CharField(max_length=500)
    parrafo_seccion7 = models.CharField(max_length=500)
    img_seccion7 = models.ImageField()
    subtitulo_seccion8 = models.CharField(max_length=500)
    parrafo_seccion8 = models.CharField(max_length=500)
    img_seccion8 = models.ImageField()
    subtitulo_seccion9 = models.CharField(max_length=500)
    parrafo_seccion9 = models.CharField(max_length=500)
    img_seccion9 = models.ImageField()
    subtitulo_seccion10 = models.CharField(max_length=500)
    parrafo_seccion10 = models.CharField(max_length=500)
    img_seccion10 = models.ImageField()
    subtitulo_seccion11 = models.CharField(max_length=500)
    parrafo_seccion11 = models.CharField(max_length=500)
    img_seccion11 = models.ImageField()

    class Meta:
        verbose_name = 'Sendero'
        verbose_name_plural = 'Sendero'

    pass
