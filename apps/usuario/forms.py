from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['dni', 'nombre', 'apellido', 'correo', 'edad', 'cargo','contraseña']
