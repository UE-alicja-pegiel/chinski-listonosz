class Vertex:

    def __init__(self, x: int, y: int, idn: str):
        self.x = x
        self.y = y
        self.idn = idn
        self.degree = 0

    def __str__(self):
        return "("+self.idn+")"

    def increase_degree(self):
        self.degree += 1

    def decrease_degree(self):
        if self.degree > 0:
            self.degree -= 1
