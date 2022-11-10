from typing import Any, Callable
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


class BinaryTree:
    root: BinaryNode

    def __init__(self, root_val):
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
