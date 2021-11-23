from django.shortcuts import render,redirect
from .forms import ProveedorForm


# Create your views here.


def Home(request):
    return render(request, 'index.html')

def agregarProveedor(request):
    if request.method== "POST":
        proveedor_form= ProveedorForm(request.POST)
        if  proveedor_form.is_valid():
            proveedor_form.save()
            return redirect('index')
    
    else: 
        proveedor_form= ProveedorForm()
    
    return render(request, 'proveedor/crearProveedor.html', {' proveedor_form':  proveedor_form})