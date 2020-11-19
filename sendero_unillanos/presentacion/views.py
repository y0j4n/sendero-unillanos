from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, DetailView

from campus.models import Campus
from contacto.models import Contacto
from educacion.models import Educacion
from presentacion.models import Presentacion
from sendero.models import Sendero


class PresentacionView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['presentaciones'] = Presentacion.objects.all()
        data['contactenos'] = Contacto.objects.all()
        return data


class EducacionView(TemplateView):
    template_name = 'educacion-ambiental.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['presentaciones'] = Presentacion.objects.all()
        data['educaciones'] = Educacion.objects.all()
        data['contactenos'] = Contacto.objects.all()
        return data


class SenderoView(TemplateView):
    template_name = 'sendero.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['presentaciones'] = Presentacion.objects.all()
        data['senderos'] = Sendero.objects.all()
        data['contactenos'] = Contacto.objects.all()
        return data

class CampusView(TemplateView):
    template_name = 'instalaciones.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['presentaciones'] = Presentacion.objects.all()
        data['instalaciones'] = Campus.objects.all()
        data['contactenos'] = Contacto.objects.all()
        return data

class GaleriaView(TemplateView):
    template_name = 'galeria.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['presentaciones'] = Presentacion.objects.all()
        data['contactenos'] = Contacto.objects.all()
        return data


class ContactoView(TemplateView):
    template_name = 'contacto.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['presentaciones'] = Presentacion.objects.all()
        data['contactenos'] = Contacto.objects.all()
        return data

