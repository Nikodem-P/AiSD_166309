from typing import Dict, List, Any, Callable
from edge import *


class Graph:
    adjcencies: Dict[Vertex, List[Edge]]

    def create_vertex(self, data: Any) -> None:
        self.adjcencies[Vertex(data)] = []

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjcencies[source].append(Edge(source, destination, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjcencies[source].append(Edge(source, destination, weight))
        self.adjcencies[destination].append(Edge(destination, source, weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == EdgeType.undirected:
            self.adjcencies[source].append(Edge(source, destination, weight))
            self.adjcencies[destination].append(Edge(destination, source, weight))
        else:
            self.adjcencies[source].append(Edge(source, destination, weight))

    def traverse_breadth_first(self, first: Vertex, visit: Callable[[Any], None]) -> None:
        queue: List[Vertex] = []
        visited: List[Vertex] = []
        queue.append(first)
        visited.append(first)
        while len(queue) != 0:
            v = queue.pop()
            visit(v)
            for x in self.adjcencies[v]:
                if x.destination not in queue and x.destination not in visited:
                    visited.append(x.destination)
                    queue.append(x.destination)

    def traverse_depth_first(self, first: Vertex, visit: Callable[[Any], None], visited: List[Vertex] = None) -> None:
        if visited is None:
            visited = []
        visit(first)
        visited.append(first)
        for x in self.adjcencies[first]:
            if x.destination not in visited:
                self.traverse_depth_first(x.destination, visit, visited)
