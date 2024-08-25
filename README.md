# Sistema de Gestión de Tareas

Este proyecto consiste en un sistema de gestión de tareas que permite agregar, actualizar, marcar como completadas, eliminar y listar tareas. Se incluye una suite de pruebas unitarias para verificar el correcto funcionamiento de todas las funciones del sistema.

## Contenido del Proyecto

- `tareas.py`: Implementación del sistema de gestión de tareas.
- `test_tareas.py`: Pruebas unitarias para verificar el funcionamiento del sistema.

## Requisitos

- Python 3.6 o superior
- pytest (para ejecutar las pruebas unitarias)

## Instalación

1. **Clona el repositorio** (si aplica):
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd <DIRECTORIO_DEL_PROYECTO>
    ```

2. **Crea un entorno virtual** (opcional pero recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. **Instala las dependencias**:
    ```sh
    pip install pytest
    ```

## Uso

### Ejemplo de uso del sistema de gestión de tareas

Puedes usar el sistema importando la clase `SistemaTareas` desde `tareas.py`. Aquí tienes un ejemplo de cómo usar el sistema:

```python
from tareas import SistemaTareas

# Crear una instancia del sistema
sistema = SistemaTareas()

# Agregar una nueva tarea
sistema.agregar_tarea(1, "Hacer la compra", "alta")

# Actualizar una tarea existente
sistema.actualizar_tarea(1, "Comprar comida", "media")

# Marcar una tarea como completada
sistema.marcar_completada(1)

# Listar tareas completadas
print(sistema.listar_tareas(completadas=True))

# Eliminar una tarea
sistema.eliminar_tarea(1)
