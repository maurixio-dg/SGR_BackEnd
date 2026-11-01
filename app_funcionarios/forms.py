
from django import forms
from .models import Funcionario


class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario

        fields = [
            'nombre',
            'cargo',
            'delegacion',
            'estado'
        ]

        labels = {
            'nombre': 'Nombre del funcionario',
            'cargo': 'Cargo',
            'delegacion': 'Delegación municipal',
            'estado': 'Estado'
        }

        widgets = {

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del funcionario'
                }
            ),

            'cargo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: Coordinador Municipal'
                }
            ),

            'delegacion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: Delegación Norte'
                }
            ),

            'estado': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            )
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()

        if len(nombre) < 2:
            raise forms.ValidationError(
                'El nombre debe tener al menos 2 caracteres.'
            )

        return nombre

    def clean_cargo(self):
        cargo = self.cleaned_data['cargo'].strip()

        if len(cargo) < 3:
            raise forms.ValidationError(
                'El cargo debe tener al menos 3 caracteres.'
            )

        return cargo

    def clean_delegacion(self):
        delegacion = self.cleaned_data['delegacion'].strip()

        if len(delegacion) < 3:
            raise forms.ValidationError(
                'La delegación debe tener al menos 3 caracteres.'
            )

        return delegacion
