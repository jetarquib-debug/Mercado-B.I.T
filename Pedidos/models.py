from django.db import models
from Carritos.models import *
# Create your models here.
class Orden(models.Model):
    ESTADO_CHOICES = [
        ('pendiente_envio', 'Pendiente de Envío'),
        ('preparando_envio', 'Preparando Envío'),
        ('en_transito', 'En Tránsito'),
        ('en_reparto', 'En Reparto'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]
    
    carrito = models.ForeignKey(Carritos, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    direccion_entrega = models.CharField(max_length=200, null=True, blank=True)
    distrito_entrega = models.OneToOneField(Distrito, null=True, blank=True, on_delete=models.SET_NULL)
    provincia_entrega = models.OneToOneField(Provincia, null=True, blank=True, on_delete=models.SET_NULL)
    pais_entrega = models.OneToOneField(Pais, null=True, blank=True, on_delete=models.SET_NULL)
    fecha_envio = models.DateTimeField(null=True, blank=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=30, choices=ESTADO_CHOICES)