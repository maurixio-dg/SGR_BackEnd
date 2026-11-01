
from django.urls import path
from . import views


urlpatterns = [

    # 1. Listar y buscar seguimientos
    path(
        '',
        views.listar_seguimientos,
        name='listar_seguimientos'
    ),

    # 2. Registrar seguimiento
    path(
        'nuevo/',
        views.crear_seguimiento,
        name='crear_seguimiento'
    ),

    # 3. Modificar seguimiento
    path(
        '<int:pk>/editar/',
        views.editar_seguimiento,
        name='editar_seguimiento'
    ),

    # 4. Eliminar seguimiento
    path(
        '<int:pk>/eliminar/',
        views.eliminar_seguimiento,
        name='eliminar_seguimiento'
    ),

]
