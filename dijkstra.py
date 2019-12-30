from collections import namedtuple, deque


inf = float('inf')
Edge = namedtuple('Edge', ('start', 'end', 'cost'))


class Graph(object):

	def __init__(self, edges):
		self.edges = [Edge(start=e[0], end=e[1], cost=e[2]) for e in edges]

	@property
	def vertices(self):
		vertices = set()
		for e in self.edges:
			vertices.update((e.start, e.end))
		return vertices

	@property
	def neighbours(self):
		neighbours = {vertex: set() for vertex in self.vertices}
		for e in self.edges:
			neighbours[e.start].add((e.end, e.cost))
		return neighbours

	def dijkstra(self, source, destination):
		distances = {vertex: inf for vertex in self.vertices}
		previous_vertices = {vertex: None for vertex in self.vertices}
		distances[source] = 0
		vertices = self.vertices.copy()

		while vertices:
			current_vertex = min(vertices, key=lambda vertex: distances[vertex])
			vertices.remove(current_vertex)

			if distances[current_vertex] == inf:
				break
			for neightbour, cost in self.neighbours[current_vertex]:
				print(neightbour, cost, distances)
				alternative_route = distances[current_vertex] + cost
				if alternative_route < distances[neightbour]:
					distances[neightbour] = alternative_route
					previous_vertices[neightbour] = current_vertex

		path, current_vertex = deque(), destination
		while previous_vertices[current_vertex]:
			path.appendleft(current_vertex)
			current_vertex = previous_vertices[current_vertex]
		path.appendleft(current_vertex)
		return path


graph = Graph([
    ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
    ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
    ("e", "f", 9)])

print(graph.dijkstra("a", "e"))

# Prints:
# b 7 {'e': inf, 'a': 0, 'd': inf, 'c': inf, 'b': inf, 'f': inf}
# c 9 {'e': inf, 'a': 0, 'd': inf, 'c': inf, 'b': 7, 'f': inf}
# f 14 {'e': inf, 'a': 0, 'd': inf, 'c': 9, 'b': 7, 'f': inf}
# c 10 {'e': inf, 'a': 0, 'd': inf, 'c': 9, 'b': 7, 'f': 14}
# d 15 {'e': inf, 'a': 0, 'd': inf, 'c': 9, 'b': 7, 'f': 14}
# f 2 {'e': inf, 'a': 0, 'd': 22, 'c': 9, 'b': 7, 'f': 14}
# d 11 {'e': inf, 'a': 0, 'd': 22, 'c': 9, 'b': 7, 'f': 11}
# e 6 {'e': inf, 'a': 0, 'd': 20, 'c': 9, 'b': 7, 'f': 11}
# f 9 {'e': 26, 'a': 0, 'd': 20, 'c': 9, 'b': 7, 'f': 11}
# deque(['a', 'c', 'd', 'e'])
