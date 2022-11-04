import random

from Vertex import Vertex
from Edge import Edge


class Graph:

    def __init__(self, size_x, size_y, n):
        self.edges = []
        self.vertices = []
        self.size_x = size_x
        self.size_y = size_y
        self.n = n
        self.generate_vertices()

    def generate_vertices(self):
        for i in range(self.n):
            x = random.randrange(0, self.size_x)
            y = random.randrange(0, self.size_y)
            idn = "vertex" + str(i)
            self.vertices.append(Vertex(x, y, idn))

    def create_edge(self, head_vertex: Vertex, tail_vertex: Vertex, cost):
        self.edges.append(Edge(head_vertex, tail_vertex, cost))
        head_vertex.increase_degree()
        tail_vertex.increase_degree()

    def delete_edge(self, edge: Edge):
        edge.head.decrease_degree()
        edge.tail.decrease_degree()
        self.edges.remove(edge)

    def check_if_graph_valid(self):
        for vertex in self.vertices:
            if vertex.degree <= 1:
                return False
        return True

    def select_random_vertex(self):
        return self.vertices[random.randrange(len(self.vertices))]

    def select_different_vertex(self, vertex):
        vertex_tail = self.select_random_vertex()
        while vertex == vertex_tail:
            vertex_tail = self.select_random_vertex()
        return vertex_tail

    def generate_graph(self):
        print(self.vertices)
        while not self.check_if_graph_valid():
            for vertex in self.vertices:
                vertex_tail = self.select_different_vertex(vertex)
                self.create_edge(vertex, vertex_tail, (random.randrange(19))+1)
        for edge in self.edges:
            print(edge)
