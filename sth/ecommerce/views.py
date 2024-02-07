from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import *

from .models import *
from .Carrito import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
# creacion de usuarios para la pagina (usuarios de django)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views.decorators.http import require_POST

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
    productos = Producto.objects.get(id=producto_id)
    marcas = Marca.objects.all()
    modelos = Modelo.objects.all()

    datos = {
        'productos': productos,
        'marcas': marcas,
        'modelos': modelos,
    }
    
    return render(request, 'core/detalle-producto.html', {**datos})

def login(request):
    return render(request,'core/login.html')

from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Aquí deberías pasar tanto request como user
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

def detalleCarrito(request):
    productos= Producto.objects.all()
    datos = {
        'productos': productos
    }
    
    
    return render(request, 'core/detalle-compra.html',{**datos})

# crud productos del carrito
def agregar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id_producto)
    carrito.agregar(producto)
    return JsonResponse({'message': 'Producto agregado al carrito'})



def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('tiendaLogeado')


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('tiendaLogeado')


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('tiendaLogeado')