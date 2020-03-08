from django.db import models
from phone_field import PhoneField

# Create your models here.

class Comentario(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    asunto=models.CharField(max_length=50)
    mensaje=models.TextField(max_length=100)
    fecha=models.DateField()

class Suscripcion(models.Model):
    correo=models.EmailField(unique=True)
    fecha=models.DateField()

class Cita(models.Model):
    reservacion=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    telefono=models.CharField(max_length=15)
    fecha=models.DateField()
    mensaje=models.TextField(max_length=100)
    terminada=models.BooleanField(default=False)

class Pregunta(models.Model):
    pregunta=models.CharField(max_length=500)
    respuesta=models.CharField(max_length=1000)