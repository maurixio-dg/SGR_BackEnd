
from django import forms
from .models import Actividad


class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad

        fields = [
            'fecha',
            'funcionario',
            'actividad',
            'tipo',
            'estado',
            'evidencia'
        ]

        labels = {
            'fecha': 'Fecha de la actividad',
            'funcionario': 'Funcionario responsable',
            'actividad': 'Descripción de la actividad',
            'tipo': 'Tipo de actividad',
            'estado': 'Estado de validación',
            'evidencia': '¿Tiene evidencia registrada?'
        }

        widgets = {

            # FECHA
            'fecha': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            # FUNCIONARIO RESPONSABLE
            'funcionario': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            # DESCRIPCIÓN
            'actividad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: Reunión de coordinación municipal'
                }
            ),

            # TIPO DE ACTIVIDAD
            'tipo': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            # ESTADO DE VALIDACIÓN
            'estado': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            # EVIDENCIA
            'evidencia': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
        }

    def clean_actividad(self):

        actividad = self.cleaned_data['actividad'].strip()

        if len(actividad) < 5:
            raise forms.ValidationError(
                'La descripción debe tener al menos 5 caracteres.'
            )

        return actividad
