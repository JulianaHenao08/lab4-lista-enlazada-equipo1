# tests/test_linked_list.py
# Pruebas base escritas por el docente.
# CADA EQUIPO agregará sus propias pruebas en este archivo
# desde su rama — esto generará merge conflicts intencionales.

import pytest
from src.linked_list import LinkedList, Node


# ------------------------------------------------------------------ #
# Pruebas del docente — __str__ y __len__                             #
# ------------------------------------------------------------------ #

def test_lista_vacia_str():
    ll = LinkedList()
    assert str(ll) == "Lista vacía"


def test_lista_vacia_len():
    ll = LinkedList()
    assert len(ll) == 0


def test_node_repr():
    n = Node(42)
    assert repr(n) == "Node(42)"
  feature/delete
    
    
# ------------------------------------------------------------------ #
# Pruebas Equipo B — delete                                           #
# ------------------------------------------------------------------ #

def test_delete_elemento_existente():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    resultado = ll.delete(2)
    assert resultado is True
    assert str(ll) == "1 -> 3"


def test_delete_head():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.delete(10)
    assert ll.head.data == 20


def test_delete_elemento_inexistente():
    ll = LinkedList()
    ll.append(5)
    resultado = ll.delete(99)
    assert resultado is False
    assert len(ll) == 1


def test_delete_lista_vacia():
    ll = LinkedList()
    assert ll.delete(1) is False
=======


# ------------------------------------------------------------------ #
# Pruebas Equipo A — append                                           #
# ------------------------------------------------------------------ #

def test_append_un_elemento():
    ll = LinkedList()

    ll.append(10)

    assert ll.head is not None
    assert ll.head.data == 10
    assert ll.head.next is None
    assert len(ll) == 1
    assert str(ll) == "10"


def test_append_varios_elementos():
    ll = LinkedList()

    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert ll.head.data == 1
    assert ll.head.next.data == 2
    assert ll.head.next.next.data == 3
    assert ll.head.next.next.next is None
    assert len(ll) == 3
    assert str(ll) == "1 -> 2 -> 3"


def test_append_mantiene_el_orden_de_insercion():
    ll = LinkedList()

    valores = ["A", "B", "C"]

    for valor in valores:
        ll.append(valor)

    current = ll.head

    for valor_esperado in valores:
        assert current is not None
        assert current.data == valor_esperado
        current = current.next

    assert current is None
    assert len(ll) == 3
    assert str(ll) == "A -> B -> C"


# ------------------------------------------------------------------ #
# Pruebas Equipo C — search                                           #
# ------------------------------------------------------------------ #

def test_search_elemento_existente():
    ll = LinkedList()

    ll.append(10)
    ll.append(20)
    ll.append(30)

    nodo = ll.search(20)

    assert nodo is not None
    assert nodo.data == 20


def test_search_elemento_inexistente():
    ll = LinkedList()

    ll.append(10)
    ll.append(20)

    resultado = ll.search(99)

    assert resultado is None


def test_search_lista_vacia():
    ll = LinkedList()

    resultado = ll.search(10)

    assert resultado is None
 main
