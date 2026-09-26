from django.shortcuts import render
from .models import Funcionario


def inicio_funcionarios(request):
    return render(request, 'app_funcionarios/inicio.html')


def listar_funcionarios(request):
    busqueda = request.GET.get('buscar', '')

    funcionarios = Funcionario.objects.all()

    if busqueda:
        funcionarios = funcionarios.filter(
            nombre__icontains=busqueda
        )

    contexto = {
        'funcionarios': funcionarios,
        'busqueda': busqueda
    }

    return render(
        request,
        'app_funcionarios/listado.html',
        contexto
    )