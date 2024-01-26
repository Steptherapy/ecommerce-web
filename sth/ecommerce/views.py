from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    productos = Producto.objects.all()
    marcas = Marca.objects.all()
    modelos = Modelo.objects.all()

    datos = {
        'productos': productos,
        'marcas': marcas,
        'modelos': modelos,
    }
    
    return render(request, 'core/index.html', {**datos})

def detalleProducto(request, producto_id):
    productos = Producto.objects.get(idProducto=producto_id)
    marcas = Marca.objects.all()
    modelos = Modelo.objects.all()

    datos = {
        'productos': productos,
        'marcas': marcas,
        'modelos': modelos,
    }
    
    return render(request, 'core/detalle-producto.html', {**datos})

