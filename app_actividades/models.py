from django.db import models
from app_funcionarios.models import Funcionario


class Actividad(models.Model):
    ESTADOS = [
        ('Validada', 'Validada'),
        ('Pendiente', 'Pendiente'),
    ]

    TIPOS = [
        ('Reunión', 'Reunión'),
        ('Atención', 'Atención'),
        ('Terreno', 'Terreno'),
        ('Seguimiento', 'Seguimiento'),
    ]

    fecha = models.DateField()

    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.PROTECT,
        related_name='actividades'
    )

    actividad = models.CharField(max_length=200)

    tipo = models.CharField(
        max_length=30,
        choices=TIPOS
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='Pendiente'
    )

    evidencia = models.BooleanField(default=False)

    def __str__(self):
        return self.actividad