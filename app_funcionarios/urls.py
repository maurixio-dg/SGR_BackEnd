
from django.urls import path
from . import views


urlpatterns = [

    # 1. Página principal de Funcionarios
    path(
        '',
        views.inicio_funcionarios,
        name='inicio_funcionarios'
    ),

    # 2. Listar y buscar funcionarios
    path(
        'listado/',
        views.listar_funcionarios,
        name='listar_funcionarios'
    ),

    # 3. Registrar un nuevo funcionario
    path(
        'nuevo/',
        views.crear_funcionario,
        name='crear_funcionario'
    ),

    # 4. Modificar funcionario
    path(
        '<int:pk>/editar/',
        views.editar_funcionario,
        name='editar_funcionario'
    ),

    # 5. Eliminar funcionario
    path(
        '<int:pk>/eliminar/',
        views.eliminar_funcionario,
        name='eliminar_funcionario'
    ),

]
