
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


@login_required(login_url='login')
def inicio(request):

    usuario = request.user

    # Identificar el perfil del usuario
    if usuario.is_superuser or usuario.groups.filter(
        name='Administrador'
    ).exists():
        perfil = 'Administrador'

    elif usuario.groups.filter(
        name='Supervisor'
    ).exists():
        perfil = 'Supervisor'

    elif usuario.groups.filter(
        name='Administrativo'
    ).exists():
        perfil = 'Administrativo'

    else:
        return HttpResponseForbidden(
            'Tu usuario no tiene un perfil asignado.'
        )

    # Enviar el perfil al template
    contexto = {
        'perfil': perfil
    }

    return render(request, 'inicio.html', contexto)
