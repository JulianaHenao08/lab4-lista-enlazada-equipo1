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