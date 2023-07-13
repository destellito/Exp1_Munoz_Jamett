from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# CLASS PRODUCTO!!

class Producto(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=250)
	precio=models.IntegerField()
	imagen=models.ImageField(upload_to='')

class Carrito(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='ItemCarrito')

    def __str__(self):
        return self.user.username
    
class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.producto.nombre} - Cantidad: {self.cantidad}'

