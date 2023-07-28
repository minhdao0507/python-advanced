from turtle import color
from unicodedata import name
from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=50, blank=True)
    age = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=20)
