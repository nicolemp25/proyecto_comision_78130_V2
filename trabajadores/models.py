from django.db import models
import uuid

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    rut = models.CharField(max_length=12, unique=True)
    tienda = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
