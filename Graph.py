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
        head_vertex.increase_degree(tail_vertex)
        tail_vertex.increase_degree(head_vertex)

    def delete_edge(self, edge: Edge):
        edge.head.decrease_degree(edge.tail)
        edge.tail.decrease_degree(edge.head)
        self.edges.remove(edge)

    def check_if_graph_valid(self):
        for vertex in self.vertices:
            if vertex.degree <= 1:
                return False
        return True

    def sort_by_degree(self):
        self.vertices.sort(key=lambda x: x.degree, reverse=True)

    def generate_graph(self):
        while not self.check_if_graph_valid():
            self.sort_by_degree()
            cost = random.randrange(self.n - 1) + 1
            # for s in self.vertices:
            #     print(s)
            # print("-------------------")
            this_vertex = self.vertices[-1]
            different_vertex = self.select_different_vertex(this_vertex)
            self.create_edge(head_vertex=self.vertices[-1],
                             tail_vertex=different_vertex,
                             cost=cost)

    def print_edges(self):
        for edge in self.edges:
            print(edge)

    def print_degrees(self):
        for vertex in self.vertices:
            print(str(vertex) + " " + str(vertex.degree))

    def select_different_vertex(self, this_vertex):
        vertex_tail = self.select_random_vertex()
        while this_vertex.check_connection(vertex_tail) and vertex_tail != this_vertex:
            vertex_tail = self.select_random_vertex()
        return vertex_tail

    def select_random_vertex(self):
        return self.vertices[random.randrange(len(self.vertices))]

    def print_duplicate_edges(self):
        duplicated = []
        for edge in self.edges:
            for edge2 in self.edges:
                if edge == edge2:
                    continue
                if (edge.tail == edge2.tail and edge.head == edge2.head) \
                        or (edge.tail == edge2.head and edge.head == edge2.tail) \
                        and edge2 not in duplicated:
                    print(edge)
                    duplicated.append(edge)
                    duplicated.append(edge2)
