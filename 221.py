from time import sleep
from a_star import a_star
from dijkstra import dijkstra
from guloso import guloso

import matplotlib.pyplot as plt


class pathfinder:
    graph = {}
    fig = None
    ax = None
    
    def start_display(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

    def draw(self, path):
        for i in range(100):
            for j in range(100):
                if (i, j) in path:
                    plt.plot(i, j, 'ro')
                else:
                    plt.plot(i, j, 'bo')
        
        plt.show()

    
    def create_graph(self, size = 10):
        for i in range(size):
            for j in range(size):
                self.graph[(i, j)] = []
                if i != 0:
                    self.graph[(i, j)].append((i - 1, j))
                    if j != 0:
                        self.graph[(i, j)].append((i - 1, j - 1))
                    if j != size - 1:
                        self.graph[(i, j)].append((i - 1, j + 1))
                if i != size - 1:
                    self.graph[(i, j)].append((i + 1, j))
                    if j != 0:
                        self.graph[(i, j)].append((i + 1, j - 1))
                    if j != size - 1: 
                        self.graph[(i, j)].append((i + 1, j + 1))
                if j != 0:
                    self.graph[(i, j)].append((i, j - 1))
                if j != size - 1:
                    self.graph[(i, j)].append((i, j + 1))
            
        
    def solve(self, algorithm, start, end):
        self.draw(algorithm(self.graph, start, end))
        
        
pathfinder = pathfinder()

pathfinder.create_graph()

pathfinder.start_display()

pathfinder.solve(guloso, (0, 0), (9, 9))

