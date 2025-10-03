from django.db import models

# Create your models here.
class Pais(models.Model):
    nomb_pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nomb_pais

# Departamentos
class Departamento(models.Model):
    nomb_departamento = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    def __str__(self):
        return self.nomb_departamento
    
# Provincias
class Provincia(models.Model):
    nomb_provincia = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomb_provincia

# Distritos
class Distrito(models.Model):
    nomb_distrito = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomb_distrito

# Usuarios
class Usuario(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    
    nombres = models.CharField(max_length=100, null=True, blank=True)
    apellidos = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    distrito = models.ForeignKey(Distrito, null=True, on_delete=models.SET_NULL, blank=True)
    provincia = models.ForeignKey(Provincia, null=True, on_delete=models.SET_NULL, blank=True)
    departamento = models.ForeignKey(Departamento, null=True, on_delete=models.SET_NULL, blank=True)
    pais = models.ForeignKey(Pais, null=True, on_delete=models.SET_NULL, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    dni_ce = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["apellidos", "nombres"]

    @property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"

    def __str__(self):
        return f"{self.id} - {self.nombres} {self.apellidos}"

#Imagen de perfil
class ImagenPerfil(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='perfil_imagenes/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    es_principal = models.BooleanField(default=False)


#Codigo de telefono de pais
class CodigoPais(models.Model):
    pais = models.OneToOneField(Pais, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10)
    imagen_pais= models.ImageField(upload_to='codigo_pais_imagenes/', null=True, blank=True)

    def __str__(self):
        return f"{self.pais.nomb_pais} (+{self.codigo})"