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
        """Inserta un nuevo nodo al final de la lista.

        Args:
            data: El valor a insertar.
        """
        raise NotImplementedError("Equipo A debe implementar append()")

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
        current = self.head

        while current is not None:
            if current.data == data:
                return current
            current = current.next

        return None