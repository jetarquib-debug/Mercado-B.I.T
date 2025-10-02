from django.db import models
from Carritos.models import *
from Usuarios.models import *
from Productos.models import *
# Create your models here.
# Detalles de órdenes
class DetalleOrden(models.Model):
    carrito = models.OneToOneField(Carritos, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)