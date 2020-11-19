from django.urls import path

from presentacion.views import PresentacionView, EducacionView, SenderoView, GaleriaView, ContactoView

urlpatterns = [
    # path('empresa/<int:pk>', CompanyDetailView.as_view(), name='perfil-empresa'),
    path('sendero', SenderoView.as_view(), name="sendero"),
    path('galeria', GaleriaView.as_view(), name="galeria"),
    path('contacto', ContactoView.as_view(), name="contacto"),
    path('educacion', EducacionView.as_view(), name='educacion-ambiental'),
    path('', PresentacionView.as_view(), name='index'),

]
