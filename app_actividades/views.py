import json
import os

from django.conf import settings
from django.shortcuts import render


def inicio_actividades(request):
    return render(request, 'app_actividades/inicio.html')


def listar_actividades(request):

    ruta_json = os.path.join(
        settings.BASE_DIR,
        'app_actividades',
        'data',
        'actividades.json'
    )

    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        actividades = json.load(archivo)

    contexto = {
        'actividades': actividades
    }

    return render(
        request,
        'app_actividades/listado.html',
        contexto
    )