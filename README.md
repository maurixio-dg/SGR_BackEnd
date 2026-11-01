
# SGR - Sistema de Gestión de Registros

Proyecto desarrollado con Django Framework para el ramo de Programación Back-End de INACAP.

El sistema ha evolucionado durante las evaluaciones del ramo, incorporando una base de datos relacional, operaciones CRUD, autenticación, gestión de usuarios, perfiles de acceso y recuperación de contraseñas mediante correo electrónico.

## 1. Descripción del proyecto

El Sistema de Gestión de Registros (SGR) permite administrar información relacionada con funcionarios, actividades y delegaciones municipales.

La aplicación utiliza Django como framework de desarrollo y MySQL como sistema de gestión de base de datos. Cuenta con una interfaz web que permite consultar y administrar registros de acuerdo con los permisos de cada usuario.

## 2. Tecnologías utilizadas

- Python
- Django 6.1.1
- MySQL
- Django ORM
- HTML y CSS
- Bootstrap
- JavaScript
- Git y GitHub
- Gmail SMTP
- AWS EC2 (despliegue)

## 3. Evolución del proyecto

### Evaluación 1

Se desarrolló la estructura inicial del sistema, trabajando con registros de funcionarios y actividades.

### Evaluación 2

Se incorporó una base de datos relacional MySQL, utilizando modelos y migraciones de Django.

También se implementó la administración de registros mediante Django Admin y se trabajó con control de versiones y despliegue en AWS EC2.

### Evaluación 3

Se amplió el sistema incorporando nuevos módulos y funcionalidades:

- CRUD de funcionarios.
- CRUD de actividades.
- CRUD de cargos.
- CRUD de delegaciones.
- CRUD de seguimientos.
- Administración de usuarios.
- Autenticación mediante inicio y cierre de sesión.
- Asignación de perfiles y permisos.
- Restricciones de acceso a vistas y operaciones.
- Recuperación de contraseñas mediante Gmail SMTP.
- Validación de enlaces de recuperación con tokens de Django.

## 4. Aplicaciones Django

El proyecto está organizado en las siguientes aplicaciones:

### app_funcionarios

Permite crear, consultar, modificar y eliminar registros de funcionarios.

### app_actividades

Permite administrar actividades asociadas a funcionarios, incluyendo información sobre fechas, estados y evidencias.

Cada actividad se relaciona con un funcionario mediante una clave foránea.

### app_cargos

Permite administrar el catálogo de cargos utilizados por el sistema.

### app_delegaciones

Permite registrar y administrar delegaciones, incluyendo sus datos de identificación y estado.

### app_seguimientos

Permite registrar seguimientos asociados a actividades y funcionarios.

Incluye validaciones y operaciones transaccionales para mantener la integridad de la información.

### app_usuarios

Permite administrar cuentas de usuario, asignar perfiles, modificar datos y controlar su estado.

También incorpora el proceso de recuperación de contraseñas utilizando las vistas de autenticación de Django.

## 5. Base de datos

El sistema utiliza MySQL y Django ORM.

Las principales entidades de gestión son:

- Funcionario.
- Actividad.
- Cargo.
- Delegación.
- Seguimiento.

Además, utiliza las tablas de autenticación y permisos proporcionadas por Django.

### Relaciones entre entidades

- Una actividad se encuentra asociada a un funcionario.
- Un seguimiento se relaciona con una actividad.
- Un seguimiento también se relaciona con un funcionario.

La base de datos utiliza claves foráneas para mantener la integridad referencial.

Se utilizan transacciones en operaciones que requieren actualizar registros relacionados.

## 6. Autenticación y perfiles

El sistema cuenta con tres perfiles principales:

### Administrador

Puede gestionar usuarios y realizar operaciones de administración sobre los módulos del sistema.

### Supervisor

Puede consultar y modificar registros de los módulos autorizados, además de crear actividades y seguimientos.

No tiene permisos para administrar usuarios ni eliminar registros.

### Administrativo

Dispone de acceso de consulta a los módulos autorizados.

No puede crear, modificar ni eliminar registros.

Las restricciones se aplican tanto en la interfaz como en las vistas del servidor.

## 7. Recuperación de contraseñas

El sistema incluye recuperación de contraseñas mediante correo electrónico.

El proceso funciona de la siguiente manera:

1. El usuario solicita recuperar su contraseña.
2. Django genera un enlace de recuperación con un token de seguridad.
3. El sistema envía el enlace mediante Gmail SMTP.
4. El usuario recibe el mensaje y accede al enlace.
5. Django valida el token recibido.
6. El usuario establece una nueva contraseña.
7. Puede iniciar sesión utilizando la contraseña actualizada.

Esta funcionalidad fue comprobada mediante una prueba de envío y recepción real de correo electrónico.

## 8. Seguridad

El proyecto incorpora medidas de seguridad como:

- Autenticación de usuarios mediante Django.
- Contraseñas almacenadas mediante los mecanismos de hash de Django.
- Roles y permisos diferenciados.
- Restricciones de acceso a operaciones no autorizadas.
- Protección CSRF en formularios.
- Validación de datos mediante formularios de Django.
- Claves foráneas e integridad referencial.
- Uso de variables de entorno para configuraciones sensibles.
- Recuperación de contraseñas con tokens de seguridad.

El archivo `.env` se mantiene excluido del repositorio mediante `.gitignore`.

## 9. Instalación local

### Clonar el repositorio

```bash
git clone https://github.com/maurixio-dg/SGR_BackEnd.git
cd SGR_BackEnd
```

### Crear y activar el entorno virtual

En Windows:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Instalar dependencias

```powershell
pip install -r requirements.txt
```

### Configurar la base de datos

Crear una base de datos MySQL y configurar sus datos de conexión mediante el archivo `.env`.

### Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto.

Ejemplo de variables necesarias:

```dotenv
DJANGO_SECRET_KEY=CLAVE_SECRETA_GENERADA_LOCALMENTE
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=sgr_db
DB_USER=USUARIO_MYSQL
DB_PASSWORD=CONTRASENA_MYSQL
DB_HOST=127.0.0.1
DB_PORT=3306

SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=CORREO_GMAIL
SMTP_APP_PASSWORD=CONTRASENA_DE_APLICACION
SMTP_USE_TLS=True
```

Los valores anteriores son ejemplos. Cada instalación debe utilizar sus propias credenciales.

No publicar el archivo `.env` en GitHub.

### Aplicar migraciones

```powershell
python manage.py migrate
```

### Crear un superusuario

```powershell
python manage.py createsuperuser
```

Los grupos Administrador, Supervisor y Administrativo deben configurarse con sus respectivos permisos en cada base de datos.

### Iniciar el servidor

```powershell
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

## 10. Pruebas realizadas

Durante el desarrollo de la Evaluación 3 se realizaron pruebas funcionales de:

- Creación, consulta, modificación y eliminación de registros.
- Relaciones entre funcionarios, actividades y seguimientos.
- Gestión de usuarios y asignación de perfiles.
- Restricción de acceso al módulo de usuarios.
- Bloqueo de creación y modificación de actividades para Administrativo.
- Bloqueo de eliminación de funcionarios para Supervisor.
- Envío de correos mediante Gmail SMTP.
- Recuperación y modificación de contraseñas.
- Inicio de sesión con la nueva contraseña.
- Comprobación de migraciones y configuración de Django.

## 11. Control de versiones

El código fuente se administra mediante Git y GitHub.

Repositorio:

https://github.com/maurixio-dg/SGR_BackEnd

La rama principal `main` reúne el desarrollo de las evaluaciones del ramo de Programación Back-End.

## 12. Despliegue

El proyecto contempla su despliegue en AWS EC2.

Para un entorno de producción es necesario configurar adecuadamente las variables de entorno, los hosts permitidos, los archivos estáticos, la conexión a la base de datos y el servicio de correo electrónico.

Las pruebas locales no reemplazan la validación funcional del sistema una vez desplegado.

## 13. Autor

Proyecto académico desarrollado por Mauricio Díaz González.

Carrera: Analista Programador.

Institución: INACAP.

Asignatura: Programación Back-End.
