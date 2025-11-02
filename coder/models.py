from django.db import models

class Tienda(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    zona = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Tienda: {self.nombre}"


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=100, default="Sin categoría")

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}"