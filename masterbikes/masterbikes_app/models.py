from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    contrasena = models.CharField(max_length=128)  
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    rut = models.CharField(max_length=12)
    id_rol = models.IntegerField(default=1)  # 1 for user, 2 for admin

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)  
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    marca = models.CharField(max_length=100)
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    id_categoria = models.AutoField(primary_key=True)
    def __str__(self):
        return self.nombre