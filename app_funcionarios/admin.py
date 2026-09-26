from django.contrib import admin
from .models import Funcionario


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'cargo',
        'delegacion',
        'estado'
    )

    search_fields = (
        'nombre',
        'cargo',
        'delegacion'
    )

    list_filter = (
        'estado',
        'delegacion'
    )