from django.db import models


usuario_cargo = [
    (1, 'Administrador'),
    (2, 'Contador'),
    (3, 'Control de Inventarios'),
    (4, 'Servicio Tecnico'),
]


class Usuario(models.Model):
    dni = models.IntegerField(primary_key=True, null=False, blank=True, verbose_name='DNI')
    nombre = models.CharField(blank=True, max_length=100, verbose_name='Nombre')
    apellido = models.CharField(blank=True, max_length=100, verbose_name='Apellido')
    correo = models.CharField(blank=True, max_length=100, verbose_name='Correo')
    edad = models.IntegerField(null=True, blank=True,verbose_name='Edad')
    cargo = models.IntegerField(null=True, blank=True, choices=usuario_cargo, verbose_name='Cargo')
    contraseña = models.CharField(blank=True, max_length=100, verbose_name='Contraseña')


    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
