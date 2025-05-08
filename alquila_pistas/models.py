from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    location = models.CharField(max_length=50)
    gender_type = models.CharField(max_length=20, default=" ", choices=[
        ('male', 'Masculino'),
        ('female', 'Feminino'),
        ('binary', 'Binario'),
    ])

    def __str__(self):
        return f"{self.name}, {self.age}, {self.location}, {self.gender_type}"

class Court(models.Model):
    name = models.CharField(max_length=50, default=" ")
    location = models.CharField(max_length=50, default=" ")
    court_type = models.CharField(max_length=50, choices=[
        ('Sports pavilion', 'Pabellon_deportivo'),
        ('beach', 'Playa'),
    ])

    def __str__(self):
        return f"{self.name}, {self.location}, {self.court_type}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user}, {self.court}, {self.date}, {self.start_time}, {self.finish_time}"

class Group(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.court.name}"