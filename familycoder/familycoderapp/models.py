from pickle import TRUE
from django.db import models

class familiar(models.Model):
    id = models.AutoField(primary_key=TRUE)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    dni = models.IntegerField()
    peso = models.IntegerField()
    altura = models.IntegerField()
