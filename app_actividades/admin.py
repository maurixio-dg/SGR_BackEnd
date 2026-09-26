from django.contrib import admin
from .models import Actividad


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fecha',
        'funcionario',
        'actividad',
        'tipo',
        'estado',
        'evidencia'
    )

    search_fields = (
        'actividad',
        'funcionario__nombre'
    )

    list_filter = (
        'tipo',
        'estado',
        'evidencia'
    )