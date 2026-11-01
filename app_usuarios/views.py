
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import UsuarioCrearForm, UsuarioEditarForm


Usuario = get_user_model()


def verificar_administrador(request):
    """
    Permite gestionar usuarios solamente a los administradores.
    """

    es_administrador = (
        request.user.is_superuser
        or request.user.groups.filter(
            name='Administrador'
        ).exists()
    )

    if not es_administrador:
        raise PermissionDenied(
            'No tienes permisos para administrar usuarios.'
        )


def validar_administrador_restante(usuario, nuevo_grupo, activo):
    """
    Evita desactivar o cambiar el rol del ultimo
    administrador activo del grupo Administrador.
    """

    es_administrador = usuario.groups.filter(
        name='Administrador'
    ).exists()

    if not usuario.is_active or not es_administrador:
        return True

    conserva_administrador = (
        activo and nuevo_grupo.name == 'Administrador'
    )

    if conserva_administrador:
        return True

    otros_administradores = Usuario.objects.filter(
        is_active=True,
        groups__name='Administrador'
    ).exclude(pk=usuario.pk).exists()

    return otros_administradores


@login_required
def listar_usuarios(request):

    verificar_administrador(request)

    busqueda = request.GET.get('q', '').strip()

    usuarios = Usuario.objects.prefetch_related(
        'groups'
    ).order_by('username')

    if busqueda:
        usuarios = usuarios.filter(
            Q(username__icontains=busqueda)
            | Q(first_name__icontains=busqueda)
            | Q(last_name__icontains=busqueda)
            | Q(email__icontains=busqueda)
        )

    contexto = {
        'usuarios': usuarios,
        'busqueda': busqueda,
    }

    return render(
        request,
        'usuarios/listado.html',
        contexto
    )


@login_required
def crear_usuario(request):

    verificar_administrador(request)

    if request.method == 'POST':
        formulario = UsuarioCrearForm(request.POST)

        if formulario.is_valid():

            with transaction.atomic():

                usuario = formulario.save()

                grupo = formulario.cleaned_data['grupo']

                usuario.groups.set([grupo])

            messages.success(
                request,
                'Usuario creado correctamente.'
            )

            return redirect('listar_usuarios')

    else:
        formulario = UsuarioCrearForm()

    contexto = {
        'formulario': formulario,
        'titulo': 'Registrar usuario',
        'boton': 'Guardar usuario',
    }

    return render(
        request,
        'usuarios/formulario.html',
        contexto
    )


@login_required
def editar_usuario(request, pk):

    verificar_administrador(request)

    usuario = get_object_or_404(Usuario, pk=pk)

    if usuario.is_superuser:
        messages.error(
            request,
            'Las cuentas de superusuario no se pueden '
            'modificar desde este formulario.'
        )

        return redirect('listar_usuarios')

    if request.method == 'POST':

        formulario = UsuarioEditarForm(
            request.POST,
            instance=usuario
        )

        if formulario.is_valid():

            grupo = formulario.cleaned_data['grupo']
            activo = formulario.cleaned_data['is_active']

            if usuario.pk == request.user.pk and not activo:

                formulario.add_error(
                    'is_active',
                    'No puedes desactivar tu propia cuenta.'
                )

            elif (
                usuario.pk == request.user.pk
                and grupo.name != 'Administrador'
            ):

                formulario.add_error(
                    'grupo',
                    'No puedes quitarte tu propio rol '
                    'de administrador.'
                )

            elif not validar_administrador_restante(
                usuario, grupo, activo
            ):

                formulario.add_error(
                    'grupo',
                    'Debe permanecer al menos un '
                    'administrador activo.'
                )

            else:

                with transaction.atomic():

                    usuario = formulario.save()

                    usuario.groups.set([grupo])

                messages.success(
                    request,
                    'Usuario actualizado correctamente.'
                )

                return redirect('listar_usuarios')

    else:
        formulario = UsuarioEditarForm(
            instance=usuario
        )

    contexto = {
        'formulario': formulario,
        'titulo': 'Editar usuario',
        'boton': 'Guardar cambios',
        'usuario_editado': usuario,
    }

    return render(
        request,
        'usuarios/formulario.html',
        contexto
    )


@login_required
@require_POST
def cambiar_estado_usuario(request, pk):

    verificar_administrador(request)

    usuario = get_object_or_404(Usuario, pk=pk)

    if usuario.is_superuser:
        messages.error(
            request,
            'No se puede desactivar ni modificar '
            'el estado de un superusuario.'
        )

        return redirect('listar_usuarios')

    if usuario.pk == request.user.pk:
        messages.error(
            request,
            'No puedes modificar el estado '
            'de tu propia cuenta.'
        )

        return redirect('listar_usuarios')

    nuevo_estado = not usuario.is_active

    grupo_actual = usuario.groups.filter(
        name='Administrador'
    ).first()

    if grupo_actual and not validar_administrador_restante(
        usuario,
        grupo_actual,
        nuevo_estado
    ):

        messages.error(
            request,
            'No puedes desactivar al ultimo '
            'administrador activo.'
        )

        return redirect('listar_usuarios')

    with transaction.atomic():

        usuario.is_active = nuevo_estado

        usuario.save(update_fields=['is_active'])

    if nuevo_estado:

        messages.success(
            request,
            'Usuario activado correctamente.'
        )

    else:

        messages.success(
            request,
            'Usuario desactivado correctamente.'
        )

    return redirect('listar_usuarios')
