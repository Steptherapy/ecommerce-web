from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('createUser/', register_view, name='register'),
    path('detalleProducto/<int:producto_id>/', detalleProducto, name='detalleProducto'),
    path('detalleCarrito/', detalleCarrito, name='detalleCarrito'),
    path("agregar/<int:id_producto>/", agregar_producto, name="Add"),
    path("eliminar/<int:id_producto>/", eliminar_producto, name="Del"),
    path("restar/<int:id_producto>/", restar_producto, name="Sub"),
    path("limpiar/", limpiar_carrito, name="Cls"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)