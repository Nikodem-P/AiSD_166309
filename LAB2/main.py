# LAB2 - LISTA JEDNOKIERUNKOWA BEZ GŁOWY
from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self):
        self.value = None
        self.next = None


class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head is None:
            print(None)
            return None
        node = self.head
        while True:
            print(f'{node.value}', end='')
            if node == self.tail:
                break
            node = node.next
            print(f' -> ', end='')

    def push(self, value: Any) -> None:
        new_node = Node()
        new_node.value = value
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def append(self, value: Any) -> None:
        new_node = Node()
        new_node.value = value
        self.tail.next = new_node
        new_node.next = None
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def pop(self) -> Any:
        if self.head is None:
            return None
        head_node_val = self.head.value
        self.head = self.head.next
        return head_node_val

    def pop_back(self) -> Any:
        if self.head is None:
            return None
        node = self.head
        while node.next != self.tail:
            node = node.next
        tail_node_val = node.next.value
        self.tail = node
        self.tail.next = None
        return tail_node_val

    def node(self, at: int) -> Any:
        if self.head is None:
            return None
        node = self.head
        for i in range(at):
            if node is None:
                return None
            node = node.next
        return node.next.value


list_ = LinkedList()
list_.push(2)
list_.append(4.45)
list_.push(3)
list_.push(7)
list_.push(7)
list_.push('abc')
list_.__str__()
print(f'\nUsuniety element z poczatku listy: {list_.pop()}')
list_.__str__()
print(f'\nUsuniety element z konca listy: {list_.pop_back()}')
list_.__str__()
print(f'\nObiekt trzeci: {list_.node(3)}')

