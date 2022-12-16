class Fleury:

    def __init__(self, graph):
        self.graph = graph
        self.edges = []
        self.shortest_path = []
        self.euler_tour = []

    def find_start(self):
        """
        :return: starting vertex to start the algorithm
        """
        for v in self.graph.vertices:
            if v.degree % 2 != 0:
                return v
        return self.graph.vertices[0]

    def order_cost(self):
        self.edges = self.graph.edges.copy()
        for j in range(1, len(self.edges)):
            key = self.edges[j]
            i = j - 1
            while i >= 0 and self.edges[i].cost > key.cost:
                self.edges[i + 1] = self.edges[i]
                i -= 1
            self.edges[i + 1] = key

    def is_bridge(self, vertex):
        return vertex.degree == 1

    def find_cost(self, start, end):
        for edge in self.graph.edges:
            if (edge.head == start and edge.tail == end) or (edge.head == end and edge.tail == start):
                return edge.cost
        return 0

    def dijkstra(self):
        self.fleury(self.find_start())
        for point in self.euler_tour:
            for edge in self.edges:
                if ((point[0] == edge.head and point[1] == edge.tail) or
                    (point[1] == edge.head and point[0] == edge.tail)) \
                        and edge not in self.shortest_path:
                    self.shortest_path.append(edge)
        return self.shortest_path

    def weights(self):
        weight = []
        w_sum = 0
        for edge in self.shortest_path:
            w_sum += edge.cost
            weight.append(w_sum)
        return weight

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

    def print_shortes_path(self):
        for e in self.shortest_path:
            print("(" + e.head.idn + ") -- " + str(e.cost) + " -- (" + e.tail.idn + ")")
