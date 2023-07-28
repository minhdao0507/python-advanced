from django.db import models
import django
# Create your models here.

class myProject(models.Model):
    name = models.CharField(max_length=200, blank=False)
    about_pro = models.CharField(max_length=500)
    tech_used = models.CharField(max_length=500)
    source = models.CharField(max_length=500)
    create_date = models.DateField(default=django.utils.timezone.now)
    status = models.CharField(max_length=10)

class User(models.Model):
    username = models.CharField(max_length = 50, unique = True)
    password = models.CharField(max_length=200,blank=True)