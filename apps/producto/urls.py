from django.urls import path
from .views import agregarProducto, listarProductos


urlpatterns = [
    path('crearProducto/', agregarProducto, name='crearProducto'),
    path('listarProductos/', listarProductos, name = 'listarProductos')
]