
from django.db import models


class Cargo(models.Model):

    ESTADOS = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    nombre = models.CharField(
        max_length=100,
        unique=True
    )

    descripcion = models.TextField(
        max_length=300
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='Activo'
    )

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.nombre
