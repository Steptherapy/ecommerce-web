from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Producto, Marca, Modelo
from .Carrito import Carrito
from .forms import LoginForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views.decorators.http import require_POST

def index(request):
    productos = Producto.objects.all()
    marcas = Marca.objects.all()
    modelos = Modelo.objects.all()

    datos = {
        'productos': productos,
        'marcas': marcas,
        'modelos': modelos,
    }
    
    return render(request, 'core/index.html', datos)

def detalleProducto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    marcas = Marca.objects.all()
    modelos = Modelo.objects.all()

    datos = {
        'producto': producto,
        'marcas': marcas,
        'modelos': modelos,
    }
    
    return render(request, 'core/detalle-producto.html', datos)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.username == 'admin':
                    return redirect('vistaAdminClientes')
                else:
                    return redirect('index')
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'loginForm': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'registerForm': form})

@login_required
def agregar_producto(request, id_producto):
    carrito = Carrito(request)
    producto ={
        'id_producto': id_producto,
    }
    producto_id = producto['id_producto']
    carrito.agregar(producto_id)
    return redirect('detalleCarrito')

@login_required
def eliminar_producto(request, id_producto):
    carrito = Carrito(request)
    producto ={
        'id_producto': id_producto,
    }
    producto_id = producto['id_producto']
    carrito.eliminar(producto_id)
    return redirect('detalleCarrito')

@login_required
def restar_producto(request, id_producto):
    carrito = Carrito(request)
    producto ={
        'id_producto': id_producto,
    }
    producto_id = producto['id_producto']
    carrito.restar(producto_id)
    return redirect('detalleCarrito')

@login_required
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('detalleCarrito')

def detalleCarrito(request):
    carrito = Carrito(request)
    productos = carrito.obtener_productos_en_carrito()
    total_carrito = carrito.obtener_total_carrito()
    datos = {
        'productos': productos,
        'total_carrito': total_carrito,
    }
    return render(request, 'core/detalle-compra.html', datos)
