# Task Manager Project

## Descripción
Este proyecto es un sistema de gestión de tareas construido con Django y Django REST Framework, que permite a los usuarios crear, leer, actualizar y eliminar tareas. La aplicación también ofrece una API pública para interactuar con el sistema mediante solicitudes HTTP y envía notificaciones por correo electrónico de manera asíncrona mediante Celery.

## Cómo Empezar

### Requisitos Previos
- Python 3.x
- Pip
- Virtualenv (opcional)
- PostgreSQL
- Redis

### Instalación

1. Clona el repositorio:

2. Crea y activa un entorno virtual (opcional):

3. Instala las dependencias:

pip install -r requirements.txt

4. Configura tu base de datos PostgreSQL en AWS y actualiza las credenciales en `.env`:

5. Realiza las migraciones de la base de datos:

python manage.py migrate

6. Ejecuta el servidor de desarrollo:

python manage.py runserver


### Configurar Celery

Para que las tareas asíncronas funcionen, necesitarás tener un worker de Celery en ejecución:


## Endpoints de la API

- `GET /api/tasks/`: Devuelve la lista de tareas existentes.
- `POST /api/tasks/`: Crea una nueva tarea con un título y una descripción.
- `PUT /api/tasks/{id}`: Actualiza una tarea existente especificada por su ID.
- `DELETE /api/tasks/{id}`: Elimina una tarea existente especificada por su ID.

Puedes ver la documentación completa y probar los endpoints accediendo a `http://localhost:8000/swagger/`.

## Interfaz de Usuario

La aplicación incluye una interfaz de usuario simple pero funcional que permite interactuar con el sistema de gestión de tareas sin necesidad de utilizar directamente la API.

### Páginas Disponibles

- **Listado de Tareas**: La página principal muestra todas las tareas existentes y permite al usuario navegar a las acciones de crear, editar o eliminar tareas.
  - Acceder a esta página visitando `http://localhost:8000/tasks/`.

- **Crear Tarea**: A través de un formulario sencillo, el usuario puede añadir una nueva tarea al sistema.
  - Acceder al formulario de creación de tareas haciendo clic en el botón "Crear Nueva Tarea" en la página de listado de tareas.

- **Editar Tarea**: Cada tarea en la lista tiene un enlace para editar la tarea, donde se muestra un formulario pre-llenado con la información de la tarea que se puede actualizar.
  - Editar una tarea haciendo clic en el botón "Editar" junto a la tarea correspondiente en la página de listado de tareas.

- **Eliminar Tarea**: Junto a cada tarea en la página de listado hay un botón "Eliminar" que, una vez confirmado, eliminará la tarea del sistema.
  - Eliminar una tarea haciendo clic en el botón "Eliminar" y confirmando la acción en el diálogo emergente.

### Navegación

La navegación entre estas páginas se realiza a través de enlaces y botones que realizan las acciones correspondientes. No es necesario interactuar directamente con la API para realizar las operaciones básicas de gestión de tareas.


## Deuda Técnica y Mejoras Futuras

- **Dockerizar la Aplicación**: Crear un `Dockerfile` y un `docker-compose.yml` para contenerizar la aplicación y sus servicios dependientes para facilitar el despliegue y la configuración.
- **Makefile**: Para simplificar la gestión de tareas comunes del proyecto, se puede crear un `Makefile` con objetivos para iniciar el servidor, realizar pruebas, etc.
- **Autenticación de Usuarios**: Implementar un sistema de autenticación de usuarios para proteger la API y gestionar permisos.
- **Fechas de Vencimiento de Tareas**: Extender el modelo de tareas para incluir fechas de vencimiento, mejorando así la gestión de tareas.



