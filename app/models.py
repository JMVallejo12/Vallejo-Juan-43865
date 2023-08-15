from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Modelo de los hoteles
class Hotel(models.Model):
    nombre = models.CharField(max_length=50)
    estrellas = models.IntegerField()
    ubicacion = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre}"

#Modelo de la reserva de hotel
class Reserva(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha = models.DateField()
    #Esto obtiene todos los nombres de los hoteles de la base de datos
    opciones = Hotel.objects.values_list('nombre','nombre') 
    
    #Seleccion de hotel
    hotel = models.CharField(max_length=50,choices=opciones)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} {self.fecha}"


#Modelo de los restaurantes
class Restaurante(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    calificacion = models.FloatField()

    def __str__(self) -> str:
        return f"{self.nombre}"



#Modelo de las ciudades
class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    habitantes = models.CharField(max_length=50)
    superficie = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre}"

#Modelo para los lugares
class Lugar(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    precioEntrada = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre}"


#Modelo de avatar
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="perfiles")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    