from django.urls import path
from .views import agregarProveedor, editarProveedor, listarProveedor, borrarProveedor


urlpatterns = [
    path('crearProveedor/', agregarProveedor, name ='crearProveedor'),
    path('listarProveedor/', listarProveedor, name = 'listarProveedor'),
    path('editarProveedor/<int:nit>', editarProveedor, name ='editarProveedor'),
    path('borrarProveedor/<int:nit>', borrarProveedor, name ='borrarProveedor')
]