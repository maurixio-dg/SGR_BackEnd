
from django.db import models
from django.core.exceptions import ValidationError

from app_actividades.models import Actividad
from app_funcionarios.models import Funcionario


class Seguimiento(models.Model):

    RESULTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Completado', 'Completado'),
    ]

    actividad = models.ForeignKey(
        Actividad,
        on_delete=models.PROTECT,
        related_name='seguimientos'
    )

    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.PROTECT,
        related_name='seguimientos'
    )

    fecha = models.DateField()

    observacion = models.TextField(
        max_length=500
    )

    resultado = models.CharField(
        max_length=20,
        choices=RESULTADOS,
        default='Pendiente'
    )

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Seguimiento'
        verbose_name_plural = 'Seguimientos'

    def clean(self):
        super().clean()

        if self.actividad_id and self.fecha:

            if self.fecha < self.actividad.fecha:
                raise ValidationError({
                    'fecha': (
                        'La fecha del seguimiento no puede '
                        'ser anterior a la actividad.'
                    )
                })

    def __str__(self):
        return f'Seguimiento de {self.actividad}'
