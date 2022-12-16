class Fleury:

    def __init__(self, graph):
        self.graph = graph
        self.euler_tour = []

    def find_start(self):
        """
        :return: starting vertex to start the algorithm
        """
        for v in self.graph.vertices:
            if v.degree % 2 != 0:
                return v
        return self.graph.vertices[0]

    def is_bridge(self, vertex):
        return vertex.degree == 1

    def find_cost(self, start, end):
        for edge in self.graph.edges:
            if (edge.head == start and edge.tail == end) or (edge.head == end and edge.tail == start):
                return edge.cost
        return 0

    def fleury(self, start_vertex):
        edge_count = len(self.graph.edges)
        while edge_count > 0:
            for v in start_vertex.connected_vertices:
                if not self.is_bridge(v):
                    self.euler_tour.append((start_vertex, v, self.find_cost(start_vertex, v)))
                    self.graph.delete_edge_vert(start_vertex, v)
                    self.fleury(v)
            edge_count -= 1
        return self.euler_tour
