from django.urls import path
from .views import agregarProducto


urlpatterns = [
    path('crearProducto/', agregarProducto, name='crearProducto')
]