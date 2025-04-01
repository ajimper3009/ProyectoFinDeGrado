from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    location = models.CharField(max_length=50)
    gender_type = models.CharField(max_length=20, choices=[
        ('male', 'Masculino'),
        ('female', 'Feminino'),
        ('binary', 'Binario'),
    ])

    def __str__(self):
        return f"{self.name}, {self.age}, {self.location}, {self.gender_type}"

class Court(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    court_type = models.CharField(max_length=50, choices=[
        ('Sports pavilion', 'Pabellon_deportivo'),
        ('beach', 'Playa'),
    ])
    equip_type = models.CharField(max_length=50, choices=[
        ('male', 'Masculino'),
        ('female', 'Feminino'),
        ('mixed', 'Mixto'),
    ])

    def __str__(self):
        return f"{self.court_type}, {self.court_type}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user}, {self.court}, {self.date}, {self.start_time}, {self.finish_time}"