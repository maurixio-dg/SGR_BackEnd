
from django.db import models


class Delegacion(models.Model):

    ESTADOS = [
        ('Activa', 'Activa'),
        ('Inactiva', 'Inactiva'),
    ]

    nombre = models.CharField(
        max_length=120,
        unique=True
    )

    sector = models.CharField(
        max_length=120
    )

    direccion = models.CharField(
        max_length=200
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='Activa'
    )

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Delegación'
        verbose_name_plural = 'Delegaciones'

    def __str__(self):
        return self.nombre
