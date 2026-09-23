# se define en el proyecto
# define los ENDPOINT LA url de cosumo de todas las apis

from django.urls import path
from .views import * #incluye a todas funciones que aparece en las vistas

urlpatterns=[
    #path("estudiantes/",views.estudiantes),
    path("estudiantes/",get_estudiantes,name="ObtenerEstudiantes"),
]