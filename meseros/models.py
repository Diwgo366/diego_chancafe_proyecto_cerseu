from django.db import models

# Create your models here.
class Meseros(models.Model):
    nombre = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=40)
    edad = models.IntegerField(default=0)
