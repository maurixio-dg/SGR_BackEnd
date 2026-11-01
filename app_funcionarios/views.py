
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import (
    login_required,
    permission_required
)

from django.contrib import messages
from django.db.models.deletion import ProtectedError

from .models import Funcionario
from .forms import FuncionarioForm


# 1. PÁGINA PRINCIPAL DEL MÓDULO
@login_required(login_url='login')
@permission_required(
    'app_funcionarios.view_funcionario',
    raise_exception=True
)
def inicio_funcionarios(request):

    return render(
        request,
        'app_funcionarios/inicio.html'
    )


# 2. LISTAR Y BUSCAR FUNCIONARIOS
@login_required(login_url='login')
@permission_required(
    'app_funcionarios.view_funcionario',
    raise_exception=True
)
def listar_funcionarios(request):

    busqueda = request.GET.get('buscar', '').strip()

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


# 3. REGISTRAR FUNCIONARIO
@login_required(login_url='login')
@permission_required(
    'app_funcionarios.add_funcionario',
    raise_exception=True
)
def crear_funcionario(request):

    if request.method == 'POST':

        formulario = FuncionarioForm(request.POST)

        if formulario.is_valid():

            formulario.save()

            messages.success(
                request,
                'Funcionario registrado correctamente.'
            )

            return redirect('listar_funcionarios')

    else:
        formulario = FuncionarioForm()

    contexto = {
        'formulario': formulario,
        'titulo': 'Registrar funcionario',
        'texto_boton': 'Guardar funcionario'
    }

    return render(
        request,
        'app_funcionarios/formulario.html',
        contexto
    )


# 4. MODIFICAR FUNCIONARIO
@login_required(login_url='login')
@permission_required(
    'app_funcionarios.change_funcionario',
    raise_exception=True
)
def editar_funcionario(request, pk):

    funcionario = get_object_or_404(
        Funcionario,
        pk=pk
    )

    if request.method == 'POST':

        formulario = FuncionarioForm(
            request.POST,
            instance=funcionario
        )

        if formulario.is_valid():

            formulario.save()

            messages.success(
                request,
                'Funcionario modificado correctamente.'
            )

            return redirect('listar_funcionarios')

    else:
        formulario = FuncionarioForm(
            instance=funcionario
        )

    contexto = {
        'formulario': formulario,
        'titulo': 'Modificar funcionario',
        'texto_boton': 'Guardar cambios'
    }

    return render(
        request,
        'app_funcionarios/formulario.html',
        contexto
    )


# 5. ELIMINAR FUNCIONARIO
@login_required(login_url='login')
@permission_required(
    'app_funcionarios.delete_funcionario',
    raise_exception=True
)
def eliminar_funcionario(request, pk):

    funcionario = get_object_or_404(
        Funcionario,
        pk=pk
    )

    if request.method == 'POST':

        try:
            funcionario.delete()

            messages.success(
                request,
                'Funcionario eliminado correctamente.'
            )

        except ProtectedError:

            messages.error(
                request,
                'No se puede eliminar este funcionario '
                'porque tiene actividades asociadas.'
            )

        return redirect('listar_funcionarios')

    contexto = {
        'funcionario': funcionario
    }

    return render(
        request,
        'app_funcionarios/confirmar_eliminar.html',
        contexto
    )
