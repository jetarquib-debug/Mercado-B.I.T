from django.db import models
from Usuarios.models import *
from Tiendas.models import *
# Marca
class Marca(models.Model):
    nomb_marca = models.CharField(max_length=100, unique=True)
    imagen_marca = models.ImageField(upload_to='marcas_imagenes/', null=True, blank=True)

    def __str__(self):
        return self.nomb_marca

# Categoria
class Categoria(models.Model):
    nomb_ca = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    imagen_categoria = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nomb_ca

# Productos
class Producto(models.Model):
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('agotado', 'Agotado'),
        ('preventa', 'Preventa'),
        ('reacondicionado', 'Reacondicionado'),
        ('descargable', 'Descargable'),
    ]
    
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    nomb_prod = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    marca = models.ForeignKey(Marca, null=True, on_delete=models.SET_NULL)
    categoria=models.ManyToManyField(Categoria)

    def __str__(self):
        return self.nomb_prod

# Imagenes de productos
class Imagen_Producto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos_imagenes/')
    es_principal = models.BooleanField(default=False)
    fecha_subida = models.DateTimeField(auto_now_add=True)