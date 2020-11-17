from django.contrib import admin

# Register your models here.
from galeria.models import Galeria, Flora, Fauna, Videos, Fotos


@admin.register(Flora)
class FloraAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'img']
    list_display_links = ['nombre', 'img']


@admin.register(Fauna)
class FaunaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'img']
    list_display_links = ['nombre', 'img']


@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'video']
    list_display_links = ['nombre', 'video']


@admin.register(Fotos)
class FotosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'img']
    list_display_links = ['nombre', 'img']


admin.site.register(Galeria)
