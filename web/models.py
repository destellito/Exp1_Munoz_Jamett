from django.db import models

# Create your models here.

# CLASS PRODUCTO!!

class Producto(models.Model):
	nombre=models.CharField(max_length=50)
	precio=models.IntegerField()
	imagen=models.ImageField(upload_to='productos/')