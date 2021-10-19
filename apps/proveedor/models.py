from django.db import models

# Create your models here.


class Proveedor(models.Model):
    nit = models.IntegerField(primary_key=True, null=False, blank=True, verbose_name='Nit')
    nombre = models.CharField(blank=True, max_length=100, verbose_name='Nombre')
    direccion = models.CharField(blank=True, max_length=100, verbose_name='Dierccion')
    correo = models.CharField(blank=True, max_length=100, verbose_name='Correo')
    numero = models.IntegerField(null=True, blank=True, verbose_name='Numero de contacto')

    def __str__(self):
        return self.nit

    class Meta:
        ordering = ['nit']
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'