
from django import forms
from .models import Cargo


class CargoForm(forms.ModelForm):

    class Meta:
        model = Cargo

        fields = [
            'nombre',
            'descripcion',
            'estado'
        ]

        labels = {
            'nombre': 'Nombre del cargo',
            'descripcion': 'Descripción del cargo',
            'estado': 'Estado'
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: Coordinador Municipal'
                }
            ),

            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Describa las funciones del cargo',
                    'rows': 4
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

        # Evitar nombres repetidos aunque cambien mayúsculas
        existentes = Cargo.objects.filter(
            nombre__iexact=nombre
        )

        if self.instance.pk:
            existentes = existentes.exclude(
                pk=self.instance.pk
            )

        if existentes.exists():
            raise forms.ValidationError(
                'Ya existe un cargo registrado con este nombre.'
            )

        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion'].strip()

        if len(descripcion) < 10:
            raise forms.ValidationError(
                'La descripción debe tener al menos 10 caracteres.'
            )

        return descripcion
