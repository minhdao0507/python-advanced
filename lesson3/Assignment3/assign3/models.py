
from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.SmallIntegerField()

class Manufactuer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, unique=True)
    address = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufactuer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    year_manufacture = models.SmallIntegerField()
    seat = models.SmallIntegerField()
