from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.inicio_funcionarios,
        name='inicio_funcionarios'
    ),

    path(
        'listado/',
        views.listar_funcionarios,
        name='listar_funcionarios'
    ),
]