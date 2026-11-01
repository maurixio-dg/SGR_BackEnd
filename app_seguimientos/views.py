
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib import messages

from django.contrib.auth.decorators import (
    login_required,
    permission_required
)

from django.db import transaction
from django.db.models import Q

from app_actividades.models import Actividad

from .models import Seguimiento
from .forms import SeguimientoForm


# 1. LISTAR Y BUSCAR SEGUIMIENTOS
@login_required(login_url='login')
@permission_required(
    'app_seguimientos.view_seguimiento',
    raise_exception=True
)
def listar_seguimientos(request):

    busqueda = request.GET.get(
        'buscar', ''
    ).strip()

    seguimientos = Seguimiento.objects.select_related(
        'actividad',
        'funcionario'
    ).all()

    if busqueda:

        seguimientos = seguimientos.filter(
            Q(actividad__actividad__icontains=busqueda) |
            Q(funcionario__nombre__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )

    contexto = {
        'seguimientos': seguimientos,
        'busqueda': busqueda
    }

    return render(
        request,
        'app_seguimientos/listado.html',
        contexto
    )


# 2. REGISTRAR SEGUIMIENTO
@login_required(login_url='login')
@permission_required(
    'app_seguimientos.add_seguimiento',
    raise_exception=True
)
def crear_seguimiento(request):

    if request.method == 'POST':

        formulario = SeguimientoForm(request.POST)

        if formulario.is_valid():

            # TRANSACCIÓN ATÓMICA
            with transaction.atomic():

                # Guardar el seguimiento
                seguimiento = formulario.save()

                # Si está completado, validar actividad
                if seguimiento.resultado == 'Completado':

                    Actividad.objects.filter(
                        pk=seguimiento.actividad_id
                    ).update(
                        estado='Validada'
                    )

            messages.success(
                request,
                'Seguimiento registrado correctamente.'
            )

            return redirect('listar_seguimientos')

    else:
        formulario = SeguimientoForm()

    contexto = {
        'formulario': formulario,
        'titulo': 'Registrar seguimiento',
        'texto_boton': 'Guardar seguimiento'
    }

    return render(
        request,
        'app_seguimientos/formulario.html',
        contexto
    )


# 3. MODIFICAR SEGUIMIENTO
@login_required(login_url='login')
@permission_required(
    'app_seguimientos.change_seguimiento',
    raise_exception=True
)
def editar_seguimiento(request, pk):

    seguimiento = get_object_or_404(
        Seguimiento,
        pk=pk
    )

    if request.method == 'POST':

        formulario = SeguimientoForm(
            request.POST,
            instance=seguimiento
        )

        if formulario.is_valid():

            # TRANSACCIÓN ATÓMICA
            with transaction.atomic():

                # Actualizar seguimiento
                seguimiento = formulario.save()

                # Actualizar actividad relacionada
                if seguimiento.resultado == 'Completado':

                    Actividad.objects.filter(
                        pk=seguimiento.actividad_id
                    ).update(
                        estado='Validada'
                    )

            messages.success(
                request,
                'Seguimiento modificado correctamente.'
            )

            return redirect('listar_seguimientos')

    else:
        formulario = SeguimientoForm(
            instance=seguimiento
        )

    contexto = {
        'formulario': formulario,
        'titulo': 'Modificar seguimiento',
        'texto_boton': 'Guardar cambios'
    }

    return render(
        request,
        'app_seguimientos/formulario.html',
        contexto
    )


# 4. ELIMINAR SEGUIMIENTO
@login_required(login_url='login')
@permission_required(
    'app_seguimientos.delete_seguimiento',
    raise_exception=True
)
def eliminar_seguimiento(request, pk):

    seguimiento = get_object_or_404(
        Seguimiento,
        pk=pk
    )

    if request.method == 'POST':

        with transaction.atomic():

            seguimiento.delete()

        messages.success(
            request,
            'Seguimiento eliminado correctamente.'
        )

        return redirect('listar_seguimientos')

    contexto = {
        'seguimiento': seguimiento
    }

    return render(
        request,
        'app_seguimientos/confirmar_eliminar.html',
        contexto
    )
