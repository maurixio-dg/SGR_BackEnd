
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

from .models import Cargo
from .forms import CargoForm


# 1. LISTAR Y BUSCAR CARGOS
@login_required(login_url='login')
@permission_required(
    'app_cargos.view_cargo',
    raise_exception=True
)
def listar_cargos(request):

    busqueda = request.GET.get('buscar', '').strip()

    cargos = Cargo.objects.all()

    if busqueda:
        cargos = cargos.filter(
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda)
        )

    contexto = {
        'cargos': cargos,
        'busqueda': busqueda
    }

    return render(
        request,
        'app_cargos/listado.html',
        contexto
    )


# 2. CREAR CARGO
@login_required(login_url='login')
@permission_required(
    'app_cargos.add_cargo',
    raise_exception=True
)
def crear_cargo(request):

    if request.method == 'POST':
        formulario = CargoForm(request.POST)

        if formulario.is_valid():
            formulario.save()

            messages.success(
                request,
                'Cargo registrado correctamente.'
            )

            return redirect('listar_cargos')

    else:
        formulario = CargoForm()

    contexto = {
        'formulario': formulario,
        'titulo': 'Registrar cargo municipal',
        'texto_boton': 'Guardar cargo'
    }

    return render(
        request,
        'app_cargos/formulario.html',
        contexto
    )


# 3. MODIFICAR CARGO
@login_required(login_url='login')
@permission_required(
    'app_cargos.change_cargo',
    raise_exception=True
)
def editar_cargo(request, pk):

    cargo = get_object_or_404(
        Cargo,
        pk=pk
    )

    if request.method == 'POST':
        formulario = CargoForm(
            request.POST,
            instance=cargo
        )

        if formulario.is_valid():
            formulario.save()

            messages.success(
                request,
                'Cargo modificado correctamente.'
            )

            return redirect('listar_cargos')

    else:
        formulario = CargoForm(
            instance=cargo
        )

    contexto = {
        'formulario': formulario,
        'titulo': 'Modificar cargo municipal',
        'texto_boton': 'Guardar cambios'
    }

    return render(
        request,
        'app_cargos/formulario.html',
        contexto
    )


# 4. ELIMINAR CARGO
@login_required(login_url='login')
@permission_required(
    'app_cargos.delete_cargo',
    raise_exception=True
)
def eliminar_cargo(request, pk):

    cargo = get_object_or_404(
        Cargo,
        pk=pk
    )

    if request.method == 'POST':
        cargo.delete()

        messages.success(
            request,
            'Cargo eliminado correctamente.'
        )

        return redirect('listar_cargos')

    return render(
        request,
        'app_cargos/confirmar_eliminar.html',
        {
            'cargo': cargo
        }
    )
