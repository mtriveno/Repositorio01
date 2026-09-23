
#el archivo se lo crea en cada proyecto
from rest_framework import serializers
from .models import Estudiantes #llama al objeto modelo

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = ['etdid','etdnombre','etdcurso','etdnota']#"__all__"