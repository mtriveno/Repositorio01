from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Estudiantes
from .serializers import EstudianteSerializer

@api_view(["GET"]) #DENINIR QUE TIPO DE API POST O GET (GET = MOSTRAR LOS DATOS)
def get_estudiantes(request): # PARA CONTROLAR VARIOS MODELOSSE PARA DIFERNETES MODELOS PARA DIFERNETES APIS E SMEJOR USAR FUNCIONES
    listaEstudiantes=Estudiantes.objects.all() #analogo a select

    serializers=EstudianteSerializer(listaEstudiantes,many=True)

    return Response(serializers.data,status.HTTP_200_OK)



