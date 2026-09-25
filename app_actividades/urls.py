from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio_actividades, name='inicio_actividades'),
    path('listado/', views.listar_actividades, name='listar_actividades'),
]