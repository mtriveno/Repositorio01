from django.db import models

# Create your models here.
class Estudiantes(models.Model):
    etdid=models.IntegerField(primary_key=True,db_column='etdid')
    etdnombre=models.CharField(max_length=100,verbose_name="NOMBRE ESTUDIANTE")
    etdcurso=models.CharField(max_length=100,verbose_name="CURSO")
    etdnota=models.IntegerField(default=0,verbose_name="NOTA")

    class Meta:
        db_table='"api"."estudiantes"'
        managed = False
