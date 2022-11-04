class Edge:

    def __init__(self, vertex_one, vertex_two, cost):
        self.head = vertex_one
        self.tail = vertex_two
        self.cost = cost

    def __str__(self):
        return "("+self.head.idn + ") -- "+ str(self.cost) +" -- (" + self.tail.idn+")"


