from django.shortcuts import redirect, render

from apps.producto.form import ProductoForm

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