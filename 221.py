from time import sleep
from a_star import a_star
from dijkstra import dijkstra
from guloso import guloso

import matplotlib.pyplot as plt


class pathfinder:
    graph = {}
    fig = None
    ax = None
    size = 10
    step = True
    
    def __init__(self, size, step = True):
        self.size = size
        self.step = step
        
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        
        for i in range(size):
            for j in range(size):
                plt.plot(i, j, 'bo')

                

    def draw(self, path):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) in path:
                    plt.plot(i, j, 'ro')
                else:
                    plt.plot(i, j, 'bo')
        
        plt.draw()
        plt.pause(0.001)
        plt.show(block=False)
        

    
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
        if self.step == True:
            self.draw(algorithm(self.graph, start, end, self.draw))
        else:
            self.draw(algorithm(self.graph, start, end))
        
        
        
        
pathfinder = pathfinder(10)

pathfinder.create_graph()


pathfinder.solve(dijkstra, (0, 0), (9, 9))

plt.pause(5)
