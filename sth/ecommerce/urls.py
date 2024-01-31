from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('login', login_view, name='login'),
    path('accounts/login/', login_view, name='login'),
    path('detalleProducto/<int:producto_id>/', detalleProducto, name='detalleProducto'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)