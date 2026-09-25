from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('admin/', admin.site.urls),

    path(
        'funcionarios/',
        include('app_funcionarios.urls')
    ),

    path(
        'actividades/',
        include('app_actividades.urls')
    ),
]