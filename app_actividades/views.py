from django.shortcuts import render
from django.db.models import Q

from .models import Actividad


def inicio_actividades(request):
    return render(request, 'app_actividades/inicio.html')


def listar_actividades(request):
    busqueda = request.GET.get('buscar', '')

    actividades = Actividad.objects.select_related(
        'funcionario'
    ).all()

    if busqueda:
        actividades = actividades.filter(
            Q(actividad__icontains=busqueda) |
            Q(funcionario__nombre__icontains=busqueda)
        )

    contexto = {
        'actividades': actividades,
        'busqueda': busqueda
    }

    return render(
        request,
        'app_actividades/listado.html',
        contexto
    )