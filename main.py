from Graph import Graph
import matplotlib.pyplot as plt

graph = Graph(size_x=100, size_y=100, n=10)

graph.generate_graph()
graph.print_edges()
#graph.print_degrees()

plt.figure(figsize=[15, 15])
plt.title('Graf')
plt.xlabel('współrzędna x')
plt.ylabel('współrzędna y')

for edge in graph.edges:
    x = [edge.head.x, edge.tail.x]
    y = [edge.head.y, edge.tail.y]
    plt.plot(x, y, 'o--r', ms=20, alpha=.5)
    plt.xticks([0, 25, 50, 75, 100])
    plt.yticks([0, 25, 50, 75, 100])
    plt.annotate(edge.head.idn, (x[0], y[0]))
    plt.annotate(edge.tail.idn, (x[1], y[1]))
    plt.text((x[0] + x[1]) / 2, (y[0] + y[1]) / 2, edge.cost)

plt.show()

