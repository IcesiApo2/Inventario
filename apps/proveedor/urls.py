from django.urls import path
from .views import agregarProveedor

urlpatterns = [
    path('crearProveedor/', agregarProveedor, name='crearProveedor')
]