from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Categoria)
admin.site.register(Comuna)
admin.site.register(Cliente)
admin.site.register(Entrega)
admin.site.register(EstadoEntrega)
admin.site.register(Laboratorio)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(ProductoPedido)
admin.site.register(Region)
admin.site.register(TipoPago)
admin.site.register(Transporte)
admin.site.register(Venta)