from django.db import models

# Create your models here.

# CLASS PRODUCTO!!

class Producto(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=250)
	precio=models.IntegerField()
	imagen=models.FileField(upload_to='')
