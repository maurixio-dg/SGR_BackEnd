
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.db.models import Q
from django.contrib import messages

from django.contrib.auth.decorators import (
    login_required,
    permission_required
)

from .models import Actividad
from .forms import ActividadForm


# 1. PÁGINA PRINCIPAL DEL MÓDULO
@login_required(login_url='login')
@permission_required(
    'app_actividades.view_actividad',
    raise_exception=True
)
def inicio_actividades(request):

    return render(
        request,
        'app_actividades/inicio.html'
    )


# 2. LISTAR Y BUSCAR ACTIVIDADES
@login_required(login_url='login')
@permission_required(
    'app_actividades.view_actividad',
    raise_exception=True
)
def listar_actividades(request):

    busqueda = request.GET.get('buscar', '').strip()

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


# 3. REGISTRAR ACTIVIDAD
@login_required(login_url='login')
@permission_required(
    'app_actividades.add_actividad',
    raise_exception=True
)
def crear_actividad(request):

    if request.method == 'POST':

        formulario = ActividadForm(request.POST)

        if formulario.is_valid():

            formulario.save()

            messages.success(
                request,
                'Actividad registrada correctamente.'
            )

            return redirect('listar_actividades')

    else:
        formulario = ActividadForm()

    contexto = {
        'formulario': formulario,
        'titulo': 'Registrar actividad',
        'texto_boton': 'Guardar actividad'
    }

    return render(
        request,
        'app_actividades/formulario.html',
        contexto
    )


# 4. MODIFICAR ACTIVIDAD
@login_required(login_url='login')
@permission_required(
    'app_actividades.change_actividad',
    raise_exception=True
)
def editar_actividad(request, pk):

    actividad = get_object_or_404(
        Actividad,
        pk=pk
    )

    if request.method == 'POST':

        formulario = ActividadForm(
            request.POST,
            instance=actividad
        )

        if formulario.is_valid():

            formulario.save()

            messages.success(
                request,
                'Actividad modificada correctamente.'
            )

            return redirect('listar_actividades')

    else:
        formulario = ActividadForm(
            instance=actividad
        )

    contexto = {
        'formulario': formulario,
        'titulo': 'Modificar actividad',
        'texto_boton': 'Guardar cambios'
    }

    return render(
        request,
        'app_actividades/formulario.html',
        contexto
    )


# 5. ELIMINAR ACTIVIDAD
@login_required(login_url='login')
@permission_required(
    'app_actividades.delete_actividad',
    raise_exception=True
)
def eliminar_actividad(request, pk):

    actividad = get_object_or_404(
        Actividad,
        pk=pk
    )

    if request.method == 'POST':

        actividad.delete()

        messages.success(
            request,
            'Actividad eliminada correctamente.'
        )

        return redirect('listar_actividades')

    contexto = {
        'actividad': actividad
    }

    return render(
        request,
        'app_actividades/confirmar_eliminar.html',
        contexto
    )
