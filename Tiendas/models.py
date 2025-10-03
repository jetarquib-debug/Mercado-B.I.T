from django.db import models
from Usuarios.models import *
# Tiendas
class Tienda(models.Model):
    nombre_tienda = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    codigo_pais = models.OneToOneField(CodigoPais, null=True, blank=True, on_delete=models.SET_NULL)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    distrito = models.OneToOneField(Distrito, null=True, blank=True, on_delete=models.SET_NULL)
    provincia = models.OneToOneField(Provincia, null=True, blank=True, on_delete=models.SET_NULL)
    pais = models.OneToOneField(Pais, null=True, blank=True, on_delete=models.SET_NULL)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ruc = models.CharField(max_length=11, null=True, blank=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_tienda