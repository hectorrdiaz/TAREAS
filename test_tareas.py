# test_tareas.py
import pytest
from tareas import SistemaTareas

@pytest.fixture
def sistema():
    return SistemaTareas()

def test_agregar_tarea(sistema):
    sistema.agregar_tarea(1, "Hacer la compra", "alta")
    assert 1 in sistema.tareas
    assert sistema.tareas[1]["descripcion"] == "Hacer la compra"
    assert sistema.tareas[1]["prioridad"] == "alta"
    assert sistema.tareas[1]["completada"] is False

def test_agregar_tarea_existente(sistema):
    sistema.agregar_tarea(1, "Hacer la compra", "alta")
    with pytest.raises(ValueError):
        sistema.agregar_tarea(1, "Otra tarea", "baja")

def test_actualizar_tarea(sistema):
    sistema.agregar_tarea(1, "Hacer la compra", "alta")
    sistema.actualizar_tarea(1, "Comprar comida", "media")
    assert sistema.tareas[1]["descripcion"] == "Comprar comida"
    assert sistema.tareas[1]["prioridad"] == "media"

def test_actualizar_tarea_no_existente(sistema):
    with pytest.raises(KeyError):
        sistema.actualizar_tarea(1, "Descripción nueva", "baja")

def test_marcar_completada(sistema):
    sistema.agregar_tarea(1, "Hacer la compra", "alta")
    sistema.marcar_completada(1)
    assert sistema.tareas[1]["completada"] is True

def test_marcar_completada_no_existente(sistema):
    with pytest.raises(KeyError):
        sistema.marcar_completada(1)

def test_eliminar_tarea(sistema):
    sistema.agregar_tarea(1, "Hacer la compra", "alta")
    sistema.eliminar_tarea(1)
    assert 1 not in sistema.tareas

def test_eliminar_tarea_no_existente(sistema):
    with pytest.raises(KeyError):
        sistema.eliminar_tarea(1)

def test_listar_tareas(sistema):
    sistema.agregar_tarea(1, "Hacer la compra", "alta")
    sistema.agregar_tarea(2, "Limpiar la casa", "media")
    sistema.marcar_completada(1)
    assert len(sistema.listar_tareas()) == 1  # Solo la tarea no completada
    assert len(sistema.listar_tareas(completadas=True)) == 1  # Solo la tarea completada
