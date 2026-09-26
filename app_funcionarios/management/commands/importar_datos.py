import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from app_funcionarios.models import Funcionario
from app_actividades.models import Actividad


class Command(BaseCommand):
    help = 'Importa funcionarios y actividades desde JSON a MySQL'

    def handle(self, *args, **options):

        # -------------------------
        # IMPORTAR FUNCIONARIOS
        # -------------------------

        ruta_funcionarios = os.path.join(
            settings.BASE_DIR,
            'app_funcionarios',
            'data',
            'funcionarios.json'
        )

        with open(ruta_funcionarios, 'r', encoding='utf-8') as archivo:
            funcionarios_json = json.load(archivo)

        for dato in funcionarios_json:
            Funcionario.objects.update_or_create(
                id=dato['id'],
                defaults={
                    'nombre': dato['nombre'],
                    'cargo': dato['cargo'],
                    'delegacion': dato['delegacion'],
                    'estado': dato['estado'],
                }
            )

        self.stdout.write(
            self.style.SUCCESS('Funcionarios importados correctamente.')
        )

        # -------------------------
        # IMPORTAR ACTIVIDADES
        # -------------------------

        ruta_actividades = os.path.join(
            settings.BASE_DIR,
            'app_actividades',
            'data',
            'actividades.json'
        )

        with open(ruta_actividades, 'r', encoding='utf-8') as archivo:
            actividades_json = json.load(archivo)

        for dato in actividades_json:

            funcionario = Funcionario.objects.get(
                nombre=dato['funcionario']
            )

            Actividad.objects.update_or_create(
                id=dato['id'],
                defaults={
                    'fecha': dato['fecha'],
                    'funcionario': funcionario,
                    'actividad': dato['actividad'],
                    'tipo': dato['tipo'],
                    'estado': dato['estado'],
                    'evidencia': dato['evidencia'] == 'Sí',
                }
            )

        self.stdout.write(
            self.style.SUCCESS('Actividades importadas correctamente.')
        )