
from django import forms

from .models import Seguimiento


class SeguimientoForm(forms.ModelForm):

    class Meta:

        model = Seguimiento

        fields = [
            'actividad',
            'funcionario',
            'fecha',
            'observacion',
            'resultado'
        ]

        labels = {
            'actividad': 'Actividad municipal',
            'funcionario': 'Funcionario responsable',
            'fecha': 'Fecha del seguimiento',
            'observacion': 'Observaciones',
            'resultado': 'Resultado del seguimiento'
        }

        widgets = {

            # ACTIVIDAD
            'actividad': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            # FUNCIONARIO RESPONSABLE
            'funcionario': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            # FECHA
            'fecha': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            # OBSERVACIONES
            'observacion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': (
                        'Describa los avances o resultados '
                        'del seguimiento realizado'
                    ),
                    'rows': 4
                }
            ),

            # RESULTADO
            'resultado': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }

    def clean_observacion(self):

        observacion = self.cleaned_data[
            'observacion'
        ].strip()

        if len(observacion) < 10:

            raise forms.ValidationError(
                'La observación debe contener '
                'al menos 10 caracteres.'
            )

        return observacion
