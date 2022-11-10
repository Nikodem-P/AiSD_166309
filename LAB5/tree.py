from typing import Any, List, Callable, Union
import graphviz


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value: Any, children: List['TreeNode']):
        self.value = value
        self.children = children

    def __str__(self):
        return str(self.value)

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for ch in self.children:
            ch.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        q = [self]
        while len(q) > 0:
            visit(q[0])
            for ch in q[0].children:
                q.append(ch)
            q.pop()

    def check_value(self, value) -> Union['TreeNode', None]:
        if self.value == value:
            return self
        return None

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self
        for ch in self.children:
            result = ch.search(value)
            if result is not None:
                return result
        return None


class Tree:
    root: TreeNode

    def __init__(self, root: TreeNode):
        self.root = root

    @staticmethod
    def add(value: Any, parent: TreeNode):
        new = TreeNode(value, [])
        parent.add(new)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def show(self):
        dot = graphviz.Digraph('Graph')
        self.for_each_deep_first(lambda x: dot.node(str(x), str(x)))
        self.for_each_deep_first(lambda x: dot.edges([(str(x), str(a)) for a in x.children]))
        print(dot.source)
