class Vertex:

    def __init__(self, x: int, y: int, idn: str):
        self.x = x
        self.y = y
        self.idn = idn
        self.degree = 0
        self.connected_vertices = []

    def __str__(self):
        return "(" + self.idn + ")"

    def increase_degree(self, vertex):
        self.connected_vertices.append(vertex)
        self.degree += 1

    def decrease_degree(self, vertex):
        if self.degree > 0:
            self.connected_vertices.remove(vertex)
            self.degree -= 1

    def check_connection(self, vertex):
        if self.connected_vertices.__contains__(vertex):
            return True
        return False
