# tareas.py

class SistemaTareas:
    def __init__(self):
        self.tareas = {}  # Diccionario para almacenar las tareas

    def agregar_tarea(self, id_tarea, descripcion, prioridad):
        if id_tarea in self.tareas:
            raise ValueError(f"La tarea con el ID {id_tarea} ya existe.")
        self.tareas[id_tarea] = {
            "descripcion": descripcion,
            "prioridad": prioridad,
            "completada": False
        }

    def actualizar_tarea(self, id_tarea, nueva_descripcion, nueva_prioridad):
        if id_tarea not in self.tareas:
            raise KeyError(f"No existe una tarea con el ID {id_tarea}.")
        self.tareas[id_tarea].update({
            "descripcion": nueva_descripcion,
            "prioridad": nueva_prioridad
        })

    def marcar_completada(self, id_tarea):
        if id_tarea not in self.tareas:
            raise KeyError(f"No existe una tarea con el ID {id_tarea}.")
        self.tareas[id_tarea]["completada"] = True

    def eliminar_tarea(self, id_tarea):
        if id_tarea not in self.tareas:
            raise KeyError(f"No existe una tarea con el ID {id_tarea}.")
        del self.tareas[id_tarea]

    def listar_tareas(self, completadas=False):
        return [tarea for tarea in self.tareas.values() if tarea["completada"] == completadas]
