from django.db import models

# Create your models here. 
class Marca(models.Model):
    idMarca = models.AutoField(primary_key=True,
                                verbose_name='id Marca')
    nombreMarca = models.CharField(max_length=80,
                                   null=False,
                                   verbose_name='Nombre Marca')
    def __str__(self):
        return self.nombreMarca

class Modelo(models.Model):
    idModelo = models.AutoField(primary_key=True,
                                verbose_name='id Modelo')
    nombreModelo = models.CharField(max_length=80,
                                   null=False,
                                   verbose_name='Nombre Modelo')
    def __str__(self):
        return self.nombreModelo
    
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True,
                                     verbose_name='id producto')
    nombreProducto = models.CharField(max_length=80,
                              verbose_name='Nombre Producto')
    descripcionProducto = models.CharField(max_length=80,
                              verbose_name='Descripcion Producto')
    Precio = models.IntegerField(verbose_name='Precio')
    
    foto = models.ImageField(upload_to='core/img/', default='core/img/logo.png')

    modelo = models.ForeignKey(Modelo ,on_delete=models.CASCADE)    

    marca = models.ForeignKey(Marca ,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreProducto