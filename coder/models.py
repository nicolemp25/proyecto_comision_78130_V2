from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    nro_legajo = models.IntegerField(unique=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_nacimiento = models.DateField(null=True)

def __str__(self):
    return f"Estudiante: {self.nombre} - Nro Legajo: {self.nro_legajo}"


class Examenes(models.Model):
    nota = models.FloatField()
    asignatura = models.CharField(max_length=30)
    nombre_de_estudiante = models.CharField(max_length=100)