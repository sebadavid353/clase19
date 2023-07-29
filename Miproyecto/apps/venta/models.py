from django.db import models

# Create your models here.
class venta(models.Model):
    nombre = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)