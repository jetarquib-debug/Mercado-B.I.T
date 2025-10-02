from django.db import models
from Usuarios.models import *
# Create your models here.
# Carritos
class Carritos(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"
        ordering = ["fecha_creacion"]
    
    def __str__(self):
        return f"Carrito {self.id} - Usuario: {self.usuario.nombres if self.usuario else 'Anónimo'} - Fecha: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"