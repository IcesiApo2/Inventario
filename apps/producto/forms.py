from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'cantidad', 'nit_proveedor', 'precio_compra', 'precio_venta', 'tipoUnidad', 'tipoProducto', 'descripcion']