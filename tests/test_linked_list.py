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


# ------------------------------------------------------------------ #
# Pruebas Equipo C — search                                          #
# ------------------------------------------------------------------ #

def test_search_elemento_existente():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)

    nodo = ll.search(10)

    assert nodo is not None
    assert nodo.data == 10


def test_search_elemento_inexistente():
    ll = LinkedList()
    ll.append(5)

    assert ll.search(99) is None


def test_search_lista_vacia():
    ll = LinkedList()

    assert ll.search(1) is None


def test_search_ultimo_elemento():
    ll = LinkedList()

    for v in [1, 2, 3]:
        ll.append(v)

    nodo = ll.search(3)

    assert nodo is not None
    assert nodo.data == 3