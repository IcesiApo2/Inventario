from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from apps.proveedor.models import Proveedor
from .forms import ProveedorForm
from .models import Proveedor


# Create your views here.


def Home(request):
    return render(request, 'index.html')


def agregarProveedor(request):
    if request.method== "POST":
        proveedor_form= ProveedorForm(request.POST)
        if  proveedor_form.is_valid():
            proveedor_form.save()
            return redirect('proveedor:listarProveedor')
    
    else: 
        proveedor_form= ProveedorForm()
    
    return render(request, 'proveedor/crearProveedor.html', {'proveedor_form':  proveedor_form})

def listarProveedor(request):
    proveedor = Proveedor.objects.all()
    return render(request, 'proveedor/listarProveedor.html',{'proveedor': proveedor})


def editarProveedor(request, nit):
    proveedor_form= None
    error = None
    try:
        proveedor = Proveedor.objects.get(nit = nit)
        if request.method == 'GET':
            proveedor_form = ProveedorForm(instance = proveedor)
        else:
            proveedor_form = ProveedorForm(request.POST, instance= proveedor)
            if proveedor_form.is_valid():
                proveedor_form.save()
            return redirect('index')

    except ObjectDoesNotExist as e:
        error= e

    return render(request, 'proveedor/crearProveedor.html',{'proveedor_form':proveedor_form, 'error': error})

def borrarProveedor(request, nit):
    proveedor= Proveedor.objects.get(nit=nit)
    proveedor.delete()
    return redirect('proveedor:listarProveedor')