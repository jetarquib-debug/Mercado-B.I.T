from django.db import models
from Pedidos.models import *
# Create your models here.
# Métodos de pago
class MetodoPago(models.Model):
    nomb_meto = models.CharField(max_length=50, unique=True)
    imagen_metodo = models.ImageField(upload_to='metodos_pago_imagenes/', null=True, blank=True)

    def __str__(self):
        return self.nomb_meto


# Pagos
class Pago(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('procesando', 'Procesando'),
        ('completado', 'Completado'),
        ('fallido', 'Fallido'),
        ('reembolsado', 'Reembolsado'),
        ('cancelado', 'Cancelado'),
    ]
    
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    metodo = models.ForeignKey(MetodoPago, on_delete=models.SET_NULL,blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    fecha_pago = models.DateTimeField(null=True, blank=True)