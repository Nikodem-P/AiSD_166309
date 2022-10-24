from linkedlist import LinkedList
from typing import Any


class Queue:
    _storage = LinkedList()

    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        str_: str = '\n'
        for i in range(len(self._storage)):
            str_ += str(self._storage.node(i).value) + ', '
        return str_

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self):
        return self._storage.pop()

    def peek(self):
        return self._storage.head.value
