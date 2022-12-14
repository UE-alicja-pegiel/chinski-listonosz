import math


class Fleury:
    """
    z https://www.tutorialspoint.com/Fleury-s-Algorithm
    """
    def __init__(self, graph):
        self.graph = graph
        self.edges = []
        self.visited = {}
        self.visit()
        self.separate_edges()

    def visit(self):
        for v in self.graph.vertices:
            self.visited[v.idn] = False

    def separate_edges(self):
        for e in self.graph.edges:
            self.edges.append((e.head, e.tail))

    def find_start(self):
        """
        :return: the starting vertex to start algorithm
        """
        for v in self.graph.vertices:
            if v.degree % 2 != 0:
                return v
        return self.graph.vertices[0]

    def dfs(self, prev, start, visited):
        """
        :param prev: previous vertex
        :param start: start vertex
        :param visited: visited vertex list
        :return: number of nodes after dfs
        """
        count = 1
        self.visited[start.idn] = True

        for v in self.graph.vertices:
            if prev != v:
                if not self.visited[v.idn]:
                    if (start, v) in self.edges:
                        count += self.dfs(start, v, visited)
        return count

    def is_bridge(self, tail):
        if tail.degree > 1:
            return False
        return True

    def fleury(self, start):
        edge_count = len(self.graph.edges)
        vert_count = len(self.graph.vertices)
        for v in self.graph.vertices:
            self.visited[v.idn] = False
            if self.is_bridge(v):
                vert_count -= 1
                cnt = self.dfs(start, v, self.visited)
                if abs(vert_count - cnt) <= 2:
                    print(start, "--", v, " ")
                    if self.is_bridge(start):
                        vert_count -= 1
                    for e in self.graph.edges:
                        if e.head == start and e.tail == v:
                            self.graph.delete_edge(e)
                            break
                    edge_count -= 1
                    self.fleury(v)
