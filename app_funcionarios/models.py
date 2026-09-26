from django.db import models


class Funcionario(models.Model):
    ESTADOS = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    delegacion = models.CharField(max_length=100)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='Activo'
    )

    def __str__(self):
        return self.nombre