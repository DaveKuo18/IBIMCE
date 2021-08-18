from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("predicaciones/", views.predicaciones, name="predicaciones"),
    path("predicaciones/<str:anio>", views.todas_las_predicaciones, name="todas_las_predicaciones"),
    path("formulario", views.formulario, name="formulario"),
    path("enviado", views.enviar_form, name="enviado"),
    path("cielo", views.cielo, name="cielo"),
    path("sobre_nosotros", views.cielo, name="sobre_nosotros")
]