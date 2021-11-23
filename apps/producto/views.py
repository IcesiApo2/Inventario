from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from apps.producto.models import Producto
from .forms import ProductoForm
from .models import Producto

# Create your views here.

def Home(request):
    return render(request, 'index.html')


def agregarProducto(request):
    if request.method== "POST":
        producto_form= ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('producto:listarProductos')
    
    else: 
        producto_form= ProductoForm()
    
    return render(request, 'producto/crearProducto.html', {'producto_form': producto_form})


def listarProductos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/listarProductos.html',{'productos': productos})


def editarProducto(request, id):
    producto_form= None
    error = None
    try:
        producto = Producto.objects.get(id = id)
        if request.method == 'GET':
            producto_form = ProductoForm(instance = producto)
        else:
            producto_form = ProductoForm(request.POST, instance= producto)
            if producto_form.is_valid():
                producto_form.save()
            return redirect('index')

    except ObjectDoesNotExist as e:
        error= e

    return render(request, 'producto/crearProducto.html',{'producto_form':producto_form, 'error': error})

def borrarProducto(request, id):
    producto= Producto.objects.get(id=id)
    producto.delete()
    return redirect('producto:listarProductos')