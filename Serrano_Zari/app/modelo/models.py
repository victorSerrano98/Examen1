from django.db import models

# Create your models here.
class Estudiante(models.Model):
    listaGenero = (
        ('f', 'femenino'),
        ('m', 'masculino')
    )
    cedula = models.CharField(max_length=10,unique=True, null=False)
    matricula = models.CharField(max_length=10, null=False, unique=True)
    apellidos = models.CharField(max_length=70,  null=False)
    nombres = models.CharField(max_length=70,  null=False)
    genero = models.CharField(max_length=15, choices= listaGenero, null=True)
    carrera= models.CharField(null=False, max_length=20)

