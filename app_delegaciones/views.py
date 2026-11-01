
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
from django.db.models import Q

from .models import Delegacion
from .forms import DelegacionForm


# 1. LISTAR Y BUSCAR DELEGACIONES
@login_required(login_url='login')
@permission_required(
    'app_delegaciones.view_delegacion',
    raise_exception=True
)
def listar_delegaciones(request):

    busqueda = request.GET.get('buscar', '').strip()

    delegaciones = Delegacion.objects.all()

    if busqueda:
        delegaciones = delegaciones.filter(
            Q(nombre__icontains=busqueda) |
            Q(sector__icontains=busqueda) |
            Q(direccion__icontains=busqueda)
        )

    contexto = {
        'delegaciones': delegaciones,
        'busqueda': busqueda
    }

    return render(
        request,
        'app_delegaciones/listado.html',
        contexto
    )


# 2. CREAR DELEGACIÓN
@login_required(login_url='login')
@permission_required(
    'app_delegaciones.add_delegacion',
    raise_exception=True
)
def crear_delegacion(request):

    if request.method == 'POST':
        formulario = DelegacionForm(request.POST)

        if formulario.is_valid():
            formulario.save()

            messages.success(
                request,
                'Delegación registrada correctamente.'
            )

            return redirect('listar_delegaciones')

    else:
        formulario = DelegacionForm()

    contexto = {
        'formulario': formulario,
        'titulo': 'Registrar delegación',
        'texto_boton': 'Guardar delegación'
    }

    return render(
        request,
        'app_delegaciones/formulario.html',
        contexto
    )


# 3. MODIFICAR DELEGACIÓN
@login_required(login_url='login')
@permission_required(
    'app_delegaciones.change_delegacion',
    raise_exception=True
)
def editar_delegacion(request, pk):

    delegacion = get_object_or_404(
        Delegacion,
        pk=pk
    )

    if request.method == 'POST':
        formulario = DelegacionForm(
            request.POST,
            instance=delegacion
        )

        if formulario.is_valid():
            formulario.save()

            messages.success(
                request,
                'Delegación modificada correctamente.'
            )

            return redirect('listar_delegaciones')

    else:
        formulario = DelegacionForm(
            instance=delegacion
        )

    contexto = {
        'formulario': formulario,
        'titulo': 'Modificar delegación',
        'texto_boton': 'Guardar cambios'
    }

    return render(
        request,
        'app_delegaciones/formulario.html',
        contexto
    )


# 4. ELIMINAR DELEGACIÓN
@login_required(login_url='login')
@permission_required(
    'app_delegaciones.delete_delegacion',
    raise_exception=True
)
def eliminar_delegacion(request, pk):

    delegacion = get_object_or_404(
        Delegacion,
        pk=pk
    )

    if request.method == 'POST':
        delegacion.delete()

        messages.success(
            request,
            'Delegación eliminada correctamente.'
        )

        return redirect('listar_delegaciones')

    return render(
        request,
        'app_delegaciones/confirmar_eliminar.html',
        {
            'delegacion': delegacion
        }
    )
