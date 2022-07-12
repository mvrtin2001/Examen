from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length = 50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to= "productos", null=True)
    
    def __str__(self):
        return self.nombre

opciones_consultas = [
    [0, "Veterinaria"],
    [1, "Peluqueria"],
    [2, "Consulta"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    nombre_mascota = models.CharField(max_length=50)
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre

