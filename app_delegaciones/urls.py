
from django.urls import path
from . import views


urlpatterns = [

    # Listar y buscar delegaciones
    path(
        '',
        views.listar_delegaciones,
        name='listar_delegaciones'
    ),

    # Registrar nueva delegación
    path(
        'nueva/',
        views.crear_delegacion,
        name='crear_delegacion'
    ),

    # Modificar delegación
    path(
        '<int:pk>/editar/',
        views.editar_delegacion,
        name='editar_delegacion'
    ),

    # Eliminar delegación
    path(
        '<int:pk>/eliminar/',
        views.eliminar_delegacion,
        name='eliminar_delegacion'
    ),

]
