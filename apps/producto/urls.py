from django.urls import path
from .views import agregarProducto, editarProducto, listarProductos, borrarProducto


urlpatterns = [
    path('crearProducto/', agregarProducto, name ='crearProducto'),
    path('listarProductos/', listarProductos, name = 'listarProductos'),
    path('editarProducto/<int:id>', editarProducto, name ='editarProducto'),
    path('borrarProducto/<int:id>', borrarProducto, name ='borrarProducto')
]