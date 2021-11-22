from django.db import models


producto_tipoUnidad = [
    (1, 'Unidades'),
    (2, 'Paquetes'),
    (3, 'Mililitros'),
    (4, 'Gramos'),
]


producto_tipo =[
    (1, 'Meteria prima.'),
    (2, 'Pruducto en proceso.'),
    (3, 'Producto terminado.'),
    (4, 'Material de empaque.'),
]


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nombre')
    nit_proveedor = models.IntegerField(blank=True, null=True, verbose_name='Nit proveedor')
    precio_compra = models.IntegerField(blank=True, null=True, verbose_name='Precio compra')
    precio_venta = models.IntegerField(blank=True, null=True, verbose_name='Precio venta')
    tipoUnidad = models.IntegerField(null=True, blank=True, choices=producto_tipoUnidad, verbose_name='Tipo Unidad')
    tipoProducto = models.IntegerField(null=True, blank=True, choices=producto_tipo, verbose_name='Tipo Unidad')
    descripcion = models.TextField(max_length=200, null=True, blank=True, verbose_name='Descipcion')

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

