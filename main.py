from Fleury import Fleury
from Graph import Graph

import matplotlib.pyplot as plt

graph = Graph(size_x=100, size_y=100, n=5)

graph.generate_graph()
graph.print_edges()
graph.print_degrees()

graph_weights = graph.weights()

plt.figure(figsize=[10, 10])
plt.suptitle('\nGraphs\n')

for edge in graph.edges:
    plt.subplot(2, 2, 1)
    plt.title(f'\nGraph: {graph_weights[-1]}\n')
    plt.xlabel('x coordinate')
    plt.ylabel('y coordinate')
    x = [edge.head.x, edge.tail.x]
    y = [edge.head.y, edge.tail.y]
    plt.plot(x, y, 'o--r', ms=10, alpha=.5)
    plt.xticks([0, 25, 50, 75, 100])
    plt.yticks([0, 25, 50, 75, 100])
    plt.annotate(edge.head.idn, (x[0], y[0]))
    plt.annotate(edge.tail.idn, (x[1], y[1]))
    plt.text((x[0] + x[1]) / 2, (y[0] + y[1]) / 2, edge.cost)

fleury = Fleury(graph)
fleury.order_cost()
shortest_path = fleury.dijkstra()
weights = fleury.weights()
fleury.print_shortes_path()
idx = 0

for edge in shortest_path:
    plt.subplot(2, 2, 2)
    plt.title(f'\nShortest path: {weights[-1]}\n')
    plt.xlabel('x coordinate')
    plt.ylabel('y coordinate')
    x = [edge.head.x, edge.tail.x]
    y = [edge.head.y, edge.tail.y]
    plt.plot(x, y, 'o--g', ms=10, alpha=.5)
    plt.xticks([0, 25, 50, 75, 100])
    plt.yticks([0, 25, 50, 75, 100])
    plt.annotate(edge.head.idn, (x[0], y[0]))
    plt.annotate(edge.tail.idn, (x[1], y[1]))
    plt.text((x[0] + x[1]) / 2, (y[0] + y[1]) / 2, weights[idx])
    idx += 1

plt.show()
