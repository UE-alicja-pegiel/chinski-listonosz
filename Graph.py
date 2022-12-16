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

    def edge_exists(self, head_vertex: Vertex, tail_vertex: Vertex):
        for edge in self.edges:
            if (edge.head == head_vertex and edge.tail == tail_vertex) or (edge.head == tail_vertex and edge.tail ==
                                                                           head_vertex):
                return True
        return False

    def weights(self):
        weight = []
        w_sum = 0
        for edge in self.edges:
            w_sum += edge.cost
            weight.append(w_sum)
        return weight

    def create_edge(self, head_vertex: Vertex, tail_vertex: Vertex, cost):
        if head_vertex != tail_vertex and not self.edge_exists(head_vertex, tail_vertex):
            self.edges.append(Edge(head_vertex, tail_vertex, cost))
            head_vertex.increase_degree(tail_vertex)
            tail_vertex.increase_degree(head_vertex)

    def delete_edge(self, edge: Edge):
        edge.head.decrease_degree(edge.tail)
        edge.tail.decrease_degree(edge.head)
        self.edges.remove(edge)

    def delete_edge_vert(self, head_vertex: Vertex, tail_vertex: Vertex):
        for edge in self.edges:
            if edge.head == head_vertex and edge.tail == tail_vertex:
                edge.head.decrease_degree(edge.tail)
                edge.tail.decrease_degree(edge.head)
                self.edges.remove(edge)
                break

    def check_if_graph_valid(self):
        for vertex in self.vertices:
            if vertex.degree <= 1:
                return False
        return True

    def sort_by_degree(self):
        self.vertices.sort(key=lambda x: x.degree, reverse=True)

    def _generate_graph(self):
        while not self.check_if_graph_valid():
            self.sort_by_degree()
            cost = random.randrange(self.n - 1) + 1
            this_vertex = self.vertices[-1]
            different_vertex = self.select_different_vertex(this_vertex)
            self.create_edge(head_vertex=self.vertices[-1],
                             tail_vertex=different_vertex,
                             cost=cost)

    def check_if_eulerian(self):
        """
        Calculate the degree of each vertex.
        Eulerian will have all even vertices, semi-Eulerian will have exactly two odd vertices.
        :return: boolean statement
        """
        count_odd = 0
        for vertex in self.vertices:
            if vertex.degree % 2 != 0:
                count_odd += 1
        if count_odd == 2:
            return True
        if count_odd == 0:
            return True
        return False

    def generate_graph(self):
        self._generate_graph()
        while not self.check_if_eulerian():
            self._generate_graph()

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
