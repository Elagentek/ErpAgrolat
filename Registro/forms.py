from django import forms
from Usuarios.models import Usuario
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
import re


class RegistroUsuario(forms.ModelForm):
    class meta : 
        model = Usuario 
        field =['nombre', 'apellido', 'correo', 'contraseña', 'cargo', 'rut']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo Electrónico',
            'contraseña': 'Contraseña',
            'cargo': 'Cargo',
            'rut': 'RUT'
        }
        error_messages = {
            'nombre': {
                'required': 'El nombre es obligatorio.',
            },
            'apellido': {
                'required': 'El apellido es obligatorio.',
            },
            'correo': {
                'required': 'El correo electrónico es obligatorio.',
                'invalid': 'Ingrese un correo electrónico válido.'
            },
            'contraseña': {
                'required': 'La contraseña es obligatoria.',
                'min_length': 'La contraseña debe tener al menos 8 caracteres.'
            },
            'cargo': {
                'required': 'El cargo es obligatorio.',
            },
            'rut': {
                'required': 'El RUT es obligatorio.',
            }
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'})
        }
    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        if len(contraseña) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
        return make_password(contraseña)
    
    def clean_rut(self):
        rut = self.cleaned_data.get('rut')

        # Eliminar puntos y guiones
        rut = rut.replace(".", "").replace("-", "").upper()

        # Validar largo mínimo
        if len(rut) < 8 or not rut[:-1].isdigit() or not rut[-1].isalnum():
            raise ValidationError('El RUT ingresado no es válido.')

        # Separar cuerpo y dígito verificador
        cuerpo = rut[:-1]
        dv = rut[-1]

        # Formatear como xx.xxx.xxx-x
        cuerpo_formateado = f"{int(cuerpo):,}".replace(",", ".")
        rut_formateado = f"{cuerpo_formateado}-{dv}"

        # Validar formato final
        if not re.match(r'^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$', rut_formateado):
            raise ValidationError('El formato del RUT no es válido (xx.xxx.xxx-x).')

        return rut_formateado
