
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [

    # PÁGINA PRINCIPAL
    path(
        '',
        views.inicio,
        name='inicio'
    ),

    # INICIO DE SESIÓN
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html',
            redirect_authenticated_user=True,
            next_page='inicio'
        ),
        name='login'
    ),

    # CIERRE DE SESIÓN
    path(
        'logout/',
        auth_views.LogoutView.as_view(
            next_page='login'
        ),
        name='logout'
    ),

    # FUNCIONARIOS
    path(
        'funcionarios/',
        include('app_funcionarios.urls')
    ),

    # ACTIVIDADES
    path(
        'actividades/',
        include('app_actividades.urls')
    ),

    # DELEGACIONES
    path(
        'delegaciones/',
        include('app_delegaciones.urls')
    ),

    # CARGOS MUNICIPALES
    path(
        'cargos/',
        include('app_cargos.urls')
    ),

    # SEGUIMIENTOS MUNICIPALES - EVA 3
    path(
        'seguimientos/',
        include('app_seguimientos.urls')
    ),

    path('usuarios/', include('app_usuarios.urls')),

]
