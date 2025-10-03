from django.db import models
from Registro.models import *
from Pagos.models import *
from Productos.models import *

# Create your models here.
#Promociones
class Promocion(models.Model):
    producto = models.ManyToManyField(Producto)
    Categoria = models.ManyToManyField(Categoria)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    descuento_porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    metodo_pago = models.ForeignKey(MetodoPago, null=True, on_delete=models.SET_NULL)
    imagen_promocion = models.ImageField(upload_to='promociones_imagenes/', null=True, blank=True)