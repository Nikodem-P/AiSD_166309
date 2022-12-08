from graph import Graph

graph = Graph()
a = graph.create_vertex("A")
b = graph.create_vertex("B")
c = graph.create_vertex("C")
graph.add_directed_edge(a, b)
graph.add_undirected_edge(b, c)
print(graph)
graph.show()