from django.db import models

# Create your models here.
from singleton_model import SingletonModel


class Flora(models.Model):
    nombre = models.CharField(max_length=250, blank=True, null=True)
    img = models.ImageField()

    class Meta:
        verbose_name = 'Flora'
        verbose_name_plural = 'Flora'

    def __str__(self):
        return self.nombre


class Fauna(models.Model):
    nombre = models.CharField(max_length=250, blank=True, null=True)
    img = models.ImageField()

    class Meta:
        verbose_name = 'Fauna'
        verbose_name_plural = 'Fauna'

    def __str__(self):
        return self.nombre


class Videos(models.Model):
    nombre = models.CharField(max_length=250, blank=True, null=True)
    video = models.FileField()

    class Meta:
        verbose_name = 'Videos'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.nombre


class Fotos(models.Model):
    nombre = models.CharField(max_length=250, blank=True, null=True)
    img = models.ImageField()

    class Meta:
        verbose_name = 'Fotos'
        verbose_name_plural = 'Fotos'

    def __str__(self):
        return self.nombre


class Galeria(SingletonModel):
    titulo = models.CharField(max_length=250)
    flora = models.ForeignKey(Flora, on_delete=models.CASCADE)
    fauna = models.ForeignKey(Fauna, on_delete=models.CASCADE)
    videos = models.ForeignKey(Videos, on_delete=models.CASCADE)
    fotos = models.ForeignKey(Fotos, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galeria'

    pass
