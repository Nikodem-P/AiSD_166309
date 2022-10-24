from linkedlist import LinkedList
from typing import Any


class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        str_: str = '\n'
        temp: list[Any] = []
        for i in range(len(self._storage)):
            temp.append(self._storage.node(i).value)
        i = len(temp) - 1
        while i >= 0:
            str_ += f'{temp[i]}\n'
            i -= 1
        return str_

    def push(self, element: Any) -> None:
        self._storage.append(element)

    def pop(self):
        return self._storage.pop_back()

