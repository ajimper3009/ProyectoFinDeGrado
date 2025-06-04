from django.contrib.auth.models import User
from django.db import models


"""
Modelo de Perfiles de Usuarios
    Atributos:
        user: Usuario del que va a ser el perfil
        name: Nombre del usuario
        age: Edad del usuario
        location: Lugar donde vive el usuario
        gender_type: Tipo de género del usuario
        profile_image: Imagen del perfil del usuario
"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    location = models.CharField(max_length=50)
    gender_type = models.CharField(max_length=20, default=" ", choices=[
        ('male', 'Masculino'),
        ('female', 'Feminino'),
        ('binary', 'Binario'),
    ])
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.age}, {self.location}, {self.gender_type}"



"""
Modelo de Courts
    Atributos:
        name: Nombre del pista
        location: Lugar donde se encuentra la pista
        latitude: Latitud de la pista
        longitude: Longitud de la pista
        court_type: Tipo de pista
"""

class Court(models.Model):
    name = models.CharField(max_length=50, default=" ")
    location = models.CharField(max_length=100, default=" ")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    court_type = models.CharField(max_length=50, choices=[
        ('Sports pavilion', 'Pabellon_deportivo'),
        ('beach', 'Playa'),
    ])

    def __str__(self):
        return f"{self.name}, {self.location}, {self.court_type}"


"""
Modelo de Reservas
        Atributos:
            user: Usuario que realiza la reserva
            court: Pista a la que se realiza la reserva
            date: Fecha de la reserva
            start_time: Hora de inicio de la reserva
            finish_time: Hora de fin de la reserva
            name_reservation: Nombre de la reserva
"""
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    date = models.CharField(max_length=50)
    start_time = models.CharField(max_length=50)
    finish_time = models.CharField(max_length=50)
    name_reservation = models.CharField(max_length=50, default=" ")

    def __str__(self):
        return f"{self.user}, {self.court}, {self.date}, {self.start_time}, {self.finish_time}"


"""
Modelo de Grupos
    Atributos:
        name: Nombre del grupo
        users: Usuarios que pertenecen al grupo
        court: Pista al que pertenece el grupo
        reservation: Reserva al que pertenece el grupo
        description: Descripción del grupo
"""
class Group(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)
    court = models.ForeignKey(Court, on_delete=models.CASCADE, null=True, blank=True)
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
