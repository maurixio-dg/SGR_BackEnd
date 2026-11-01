
from django import forms
from .models import Delegacion


class DelegacionForm(forms.ModelForm):

    class Meta:
        model = Delegacion

        fields = [
            'nombre',
            'sector',
            'direccion',
            'estado'
        ]

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la delegación'
                }
            ),

            'sector': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Sector correspondiente'
                }
            ),

            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Dirección de la delegación'
                }
            ),

            'estado': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()

        if len(nombre) < 3:
            raise forms.ValidationError(
                'El nombre debe tener al menos 3 caracteres.'
            )

        return nombre
