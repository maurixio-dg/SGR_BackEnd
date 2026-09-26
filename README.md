# SGR - Sistema de Gestión de Registros

Proyecto desarrollado con Django Framework como evolución de la aplicación realizada en la Evaluación Sumativa N°1.

## Descripción

El sistema permite gestionar y visualizar información relacionada con funcionarios y actividades de Delegaciones Municipales.

La información es almacenada en una base de datos relacional y administrada mediante Django Admin.

## Tecnologías utilizadas

- Python
- Django
- MySQL / MariaDB
- Django ORM
- Bootstrap
- HTML
- CSS
- Git
- GitHub

## Aplicaciones Django

El proyecto está compuesto por dos aplicaciones principales:

### app_funcionarios

Permite administrar y visualizar los funcionarios registrados en el sistema.

### app_actividades

Permite administrar y visualizar las actividades asociadas a los funcionarios.

Existe una relación entre ambas entidades mediante una ForeignKey desde Actividad hacia Funcionario.

## Base de datos

La aplicación utiliza una base de datos relacional MySQL/MariaDB.

Los datos que anteriormente estaban almacenados en archivos JSON fueron migrados hacia la base de datos utilizando modelos y migraciones de Django.

## Django Admin

Las entidades Funcionario y Actividad se encuentran registradas en Django Admin.

Desde el panel de administración es posible:

- Crear registros.
- Visualizar registros.
- Modificar registros.
- Eliminar registros.
- Buscar registros.

## Variables de entorno

Las configuraciones sensibles de la base de datos son administradas mediante variables de entorno utilizando un archivo `.env`.

El archivo `.env` no se incluye en el repositorio por razones de seguridad.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/maurixio-dg/SGR_BackEnd.git