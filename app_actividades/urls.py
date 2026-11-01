
from django.urls import path
from . import views


urlpatterns = [

    # 1. Página principal del módulo
    path(
        '',
        views.inicio_actividades,
        name='inicio_actividades'
    ),

    # 2. Listar y buscar actividades
    path(
        'listado/',
        views.listar_actividades,
        name='listar_actividades'
    ),

    # 3. Registrar una nueva actividad
    path(
        'nueva/',
        views.crear_actividad,
        name='crear_actividad'
    ),

    # 4. Modificar una actividad
    path(
        '<int:pk>/editar/',
        views.editar_actividad,
        name='editar_actividad'
    ),

    # 5. Eliminar una actividad
    path(
        '<int:pk>/eliminar/',
        views.eliminar_actividad,
        name='eliminar_actividad'
    ),

]
