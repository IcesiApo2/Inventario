from django.shortcuts import redirect, render

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
            return redirect('index')
    
    else: 
        producto_form= ProductoForm()
    
    return render(request, 'producto/crearProducto.html', {'producto_form': producto_form})


def listarProductos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/listarProductos.html',{'productos': productos})