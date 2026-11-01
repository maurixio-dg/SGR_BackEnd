
from django.urls import path
from . import views


urlpatterns = [

    # Listar y buscar cargos
    path(
        '',
        views.listar_cargos,
        name='listar_cargos'
    ),

    # Registrar un nuevo cargo
    path(
        'nuevo/',
        views.crear_cargo,
        name='crear_cargo'
    ),

    # Modificar un cargo existente
    path(
        '<int:pk>/editar/',
        views.editar_cargo,
        name='editar_cargo'
    ),

    # Eliminar un cargo
    path(
        '<int:pk>/eliminar/',
        views.eliminar_cargo,
        name='eliminar_cargo'
    ),

]
