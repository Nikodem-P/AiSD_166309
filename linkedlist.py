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
        str_: str = ''
        if self.head is None:
            str_ += None
            return None
        node = self.head
        while True:
            str_ += f'{node.value}'
            if node == self.tail:
                break
            node = node.next
            str_ += f' -> '
        return str_

    def __len__(self):
        node = self.head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def push(self, value: Any) -> None:
        new_node = Node()
        new_node.value = value
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = self.head

    def append(self, value: Any) -> None:
        new_node = Node()
        new_node.value = value
        new_node.next = None
        if self.head is None:
            self.tail = new_node
            self.head = self.tail
            return None
        self.tail.next = new_node
        self.tail = new_node

    def pop(self) -> Any:
        if self.head is None:
            return None
        if self.head == self.tail:
            head_node_val = self.head.value
            self.head = None
            self.tail = None
            return head_node_val
        head_node_val = self.head.value
        self.head = self.head.next
        return head_node_val

    def pop_back(self) -> Any:
        if self.head is None:
            return None
        if self.head == self.tail:
            tail_node_val = self.head.value
            self.head = None
            self.tail = None
            return tail_node_val
        node = self.head
        while node.next != self.tail:
            node = node.next
        tail_node_val = node.next.value
        self.tail = node
        self.tail.next = None
        return tail_node_val

    def node(self, at: int) -> Node:
        if self.head is None:
            return None
        node = self.head
        for i in range(at):
            if node is None:
                return None
            node = node.next
        return node

    @staticmethod
    def insert(value: Any, after: Node) -> None:
        new_node = Node()
        new_node.value = value
        new_node.next = after.next
        after.next = new_node

    @staticmethod
    def remove(after: Node) -> None:
        after.next = after.next.next
