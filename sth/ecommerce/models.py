import datetime
from django.db import models
from django.utils.timezone import now

class Categoria(models.Model):
    nombrecategoria = models.CharField(max_length=80)
        
    def __str__(self):
        return self.nombrecategoria


class Comuna(models.Model):
    nombrecomuna = models.CharField(max_length=80)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombrecomuna

class Cliente(models.Model):
    pnombrecliente = models.CharField(max_length=80)
    snombrecliente = models.CharField(max_length=80, null=True, blank=True)
    appaternocliente = models.CharField(max_length=80)
    apmaternocliente = models.CharField(max_length=80)
    direccioncliente = models.CharField(max_length=250)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    def __str__(self):
        return (self.pnombrecliente,' ',self.appaternocliente,' ', self.apmaternocliente)

class Entrega(models.Model):
    idpedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    idestadoentrega = models.ForeignKey('EstadoEntrega', on_delete=models.CASCADE)
    idtransporte = models.ForeignKey('Transporte', on_delete=models.CASCADE)
    

class EstadoEntrega(models.Model):
    nombreestado = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nombreestado

class Laboratorio(models.Model):
    nombreLaboratorio = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nombreLaboratorio

class Marca(models.Model):
    nombreMarca = models.CharField(max_length=80)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreMarca

class Modelo(models.Model):
    nombremodelo = models.CharField(max_length=80)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombremodelo 

class Producto(models.Model):
    nombreproducto = models.CharField(max_length=80)
    numeroserieproducto = models.CharField(max_length=150)
    fechaingresoproducto = models.DateTimeField(default=now, editable=False)
    preciounitarioproducto = models.DecimalField(max_digits=9, decimal_places=2)
    imagenproducto = models.ImageField(null=True, blank=True)
    descripcionproducto = models.CharField(max_length=250)
    productoactivo = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreproducto

class Region(models.Model):
    nombreregion = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nombreregion

class TipoPago(models.Model):
    nombretipopago = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nombretipopago

class Transporte(models.Model):
    nombretransporte = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nombretransporte

class Venta(models.Model):
    fechaventa = models.DateTimeField(default=now, editable=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipopago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Pedido(models.Model):
    direccionentregapedido = models.CharField(max_length=250)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    
class ProductoPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)