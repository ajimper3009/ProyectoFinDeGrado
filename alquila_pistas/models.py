from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    location = models.CharField(max_length=50)
    gender_type = models.CharField(max_length=20, choices=[
        ('male', 'Masculino'),
        ('female', 'Feminino'),
        ('mixed', 'Mixto'),
    ])

    def __str__(self):
        return f"{self.name}, {self.age}, {self.location}, {self.gender_type}"

class Court(models.Model):
    court_type = models.CharField(max_length=50, choices=[
        ('inside', 'Interior'),
        ('outside', 'Exterior'),
    ])
    gender_type = models.CharField(max_length=20, choices=[
        ('male', 'Masculino'),
        ('female', 'Feminino'),
        ('mixed', 'Mixto'),
    ])

    def __str__(self):
        return f"{self.court_type}, {self.gender_type}"
