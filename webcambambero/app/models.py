from django.db import models

# Create your models here.

class planes(models.Model):
    nombre=models.CharField(max_length=100)
    fecha=models.DateField()
    lugar=models.CharField(max_length=100)
    creador=models.CharField(max_length=100)
    
    
