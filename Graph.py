import random

from Vertex import Vertex
from Edge import Edge

class Graph:

    def __init__(self):
        self.edges = []
        self.vertices = []

    def generate(self, n, size_x, size_y):
        for i in range(n):
            x = random.randrange(0, size_x)
            y = random.randrange(0, size_y)
            idn = "vertex" + str(i)
            self.vertices.append(Vertex(x, y, idn))

    def create_edge(self, vertex_one, vertex_two):
        self.edges.append(Edge(vertex_one, vertex_two))
        vertex_one.degree += 1
        vertex_two.degree += 1
