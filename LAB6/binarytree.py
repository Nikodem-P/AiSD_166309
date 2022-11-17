from typing import List, Any, Callable
import graphviz


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f'{self.value}'

    def is_leaf(self) -> bool:
        if self.left_child is None and self.right_child is None:
            return True
        return False

    def add_left_child(self, value: Any) -> None:
        new = BinaryNode(value)
        self.left_child = new

    def add_right_child(self, value: Any) -> None:
        new = BinaryNode(value)
        self.right_child = new

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def add_edges(self, dot: graphviz.Digraph):
        if self.left_child is not None:
            dot.edge(str(self), str(self.left_child))
        if self.right_child is not None:
            dot.edge(str(self), str(self.right_child))

    def min(self) -> 'BinaryNode':
        if self.left_child is None:
            return self
        return self.left_child.min()


class BinaryTree:
    root: BinaryNode

    def __init__(self, root_val: Any):
        self.root = BinaryNode(root_val)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def show(self):
        dot = graphviz.Digraph('Graph')
        self.traverse_in_order(lambda x: dot.node(str(x), str(x)))
        self.traverse_in_order(lambda x: x.add_edges(dot))
        print(dot.source)


class BinarySearchTree(BinaryTree):

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value < node.value:
            if node.left_child is None:
                node.left_child = BinaryNode(value)
                return node.left_child
            return self._insert(node.left_child, value)

        if node.right_child is None:
            node.right_child = BinaryNode(value)
            return node.right_child
        return self._insert(node.right_child, value)

    def insert(self, value: Any) -> None:
        self._insert(self.root, value)

    def insert_list(self, list_: List[Any]):
        for i in list_:
            self.insert(i)

    def contains(self, value: Any) -> bool:
        node = self.root
        while node.left_child is not None or node.right_child is not None:
            if node.value == value:
                return True
            elif node.value > value:
                node = node.left_child
            else:
                node = node.right_child
        return node.value == value

    def _remove(self, node: BinaryNode, value: Any):
        if value == node.value:
            if node.left_child is None:
                return node.right_child
            if node.right_child is None:
                return node.left_child
            node.value = node.right_child.min().value
            node.right_child = self._remove(node.right_child, node.right_child.value)
        if value < node.value:
            node.left_child = self._remove(node.left_child, value)
        if value > node.value:
            node.right_child = self._remove(node.right_child, value)
        return node

    def remove(self, value: Any):
        self._remove(self.root, value)
