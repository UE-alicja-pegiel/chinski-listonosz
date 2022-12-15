class Fleury:

    def __init__(self, graph):
        self.graph = graph

    def find_all_paths(self, start, end, path=None):
        """
        :param start: starting vertex
        :param end: end vertex
        :param path: path from one vertex to another
        :return: list of paths
        """
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for vertex in start.connected_vertices:
            if vertex not in path:
                newpaths = self.find_all_paths(vertex, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def reachable_vertices(self, vertex):
        """
        :param vertex: chosen vertex
        :return: all reachable vertices from the vertex
        """
        vertices = set()
        if vertex == self.graph.vertices[-1]:
            paths = self.find_all_paths(vertex, self.graph.vertices[-2])
            for path in paths:
                for v in range(len(path)):
                    vertices.add(path[v])
            return vertices
        else:
            paths = self.find_all_paths(vertex, self.graph.vertices[-1])
            for path in paths:
                for v in range(len(path)):
                    vertices.add(path[v])
            return vertices

    def find_start(self):
        """
        :return: starting vertex to start the algorithm
        """
        for v in self.graph.vertices:
            if v.degree % 2 != 0:
                return v
        return self.graph.vertices[0]

    def is_bridge(self, edge):
        """
        :param edge: edge of a graph
        :return: boolean statement if edge is a bridge or not
        """
        if len(edge.head.connected_vertices) == 1:
            return False
        else:
            head = edge.head
            tail = edge.tail
            cost = edge.cost
            count1 = len(self.reachable_vertices(edge.head))
            self.graph.delete_edge(edge)
            count2 = len(self.reachable_vertices(edge.head))
            self.graph.create_edge(head, tail, cost)
            return True if count1 > count2 else False

    def euler_tour(self, u):
        euler = []
        for e in self.graph.edges:
            if not self.is_bridge(e):
                euler.append(e)
        return euler
