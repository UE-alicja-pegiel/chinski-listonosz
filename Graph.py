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

    def check_if_already_exist(self, vertex_head, vertex_tail):
        for edge in self.edges:
            if (edge.tail == vertex_head and edge.head == vertex_tail) \
                    and not (edge.tail == vertex_tail and edge.tail == vertex_head):
                return True
        return False

    def select_different_vertex(self, vertex):
        vertex_tail = self.select_random_vertex()
        while vertex == vertex_tail and not self.check_if_already_exist(vertex_head=vertex, vertex_tail=vertex_tail):
            vertex_tail = self.select_random_vertex()
        return vertex_tail

    def generate_graph(self):
        while not self.check_if_graph_valid():
            for vertex in self.vertices:
                vertex_tail = self.select_different_vertex(vertex)
                self.create_edge(vertex, vertex_tail, (random.randrange(19)) + 1)

    def print_edges(self):
        for edge in self.edges:
            print(edge)

    def print_degrees(self):
        for vertex in self.vertices:
            print(str(vertex) + " " + str(vertex.degree))

    def print_duplicate_edges(self):
        duplicated = []
        for edge in self.edges:
            for edge2 in self.edges:
                if edge == edge2:
                    continue
                if (edge.tail == edge2.tail and edge.head == edge2.head) \
                        or (edge.tail == edge2.head and edge.head == edge2.tail) and edge2 not in duplicated:
                    print(edge)
                    duplicated.append(edge)
                    duplicated.append(edge2)
