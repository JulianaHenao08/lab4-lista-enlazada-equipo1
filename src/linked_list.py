# src/linked_list.py
# Estructura base — cada equipo implementa su operación asignada.


class Node:
    """Nodo de la lista enlazada."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """Lista enlazada simple."""

    def __init__(self):
        self.head = None

    # ------------------------------------------------------------------ #
    # Implementado por el docente — NO modificar                          #
    # ------------------------------------------------------------------ #
    def __str__(self):
        """Retorna una representación legible de la lista."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Lista vacía"

    def __len__(self):
        """Retorna el número de nodos."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # ------------------------------------------------------------------ #
    # TODO — Equipo A: rama feature/append                                #
    # ------------------------------------------------------------------ #
    
    def append(self, data):
        """Agrega un nuevo nodo con el valor data al final de la lista."""
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    # ------------------------------------------------------------------ #
    # TODO — Equipo B: rama feature/delete                                #
    # ------------------------------------------------------------------ #
    def delete(self, data):
        """Elimina el primer nodo cuyo valor sea igual a data.

        Args:
            data: El valor a eliminar.

        Returns:
            True si el nodo fue eliminado, False si no se encontró.
        """
        raise NotImplementedError("Equipo B debe implementar delete()")

    # ------------------------------------------------------------------ #
    # TODO — Equipo C: rama feature/search                                #
    # ------------------------------------------------------------------ #
    def search(self, data):
        """Busca un valor en la lista.

        Args:
            data: El valor a buscar.

        Returns:
            El nodo que contiene data, o None si no existe.
        """
        raise NotImplementedError("Equipo C debe implementar search()")