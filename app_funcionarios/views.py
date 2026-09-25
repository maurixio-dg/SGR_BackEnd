import json
import os

from django.conf import settings
from django.shortcuts import render


def inicio_funcionarios(request):
    return render(request, 'app_funcionarios/inicio.html')


def listar_funcionarios(request):

    ruta_json = os.path.join(
        settings.BASE_DIR,
        'app_funcionarios',
        'data',
        'funcionarios.json'
    )

    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        funcionarios = json.load(archivo)

    contexto = {
        'funcionarios': funcionarios
    }

    return render(
        request,
        'app_funcionarios/listado.html',
        contexto
    )