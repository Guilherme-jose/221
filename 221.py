from time import sleep
from a_star import a_star
from dijkstra import dijkstra
from guloso import guloso
import time

import matplotlib.pyplot as plt


class pathfinder:
    graph = {}
    fig = None
    ax = None
    size = 10
    step = True
    prev_path = []
    walls = []
    
    def __init__(self, size, step = True):
        self.size = size
        self.step = step
        
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        
        for i in range(size):
            for j in range(size):
                    plt.plot(i, j, 'bo')
            

                

    def draw(self, path):
        for i in path: plt.plot(i[0], i[1], 'ro')
        for i in self.prev_path:
            if i not in path: plt.plot(i[0], i[1], 'bo')
        self.prev_path = path
        
        plt.draw()
        plt.pause(0.001)
        plt.show(block=False)
        

    
    def create_graph(self):
        for i in range(self.size):
            for j in range(self.size):
                self.graph[(i, j)] = []
                if i != 0 and (i - 1, j) not in self.walls:
                    self.graph[(i, j)].append((i - 1, j))
                    if j != 0 and (i - 1, j - 1) not in self.walls:
                        self.graph[(i, j)].append((i - 1, j - 1))
                    if j != self.size - 1 and (i - 1, j + 1) not in self.walls:
                        self.graph[(i, j)].append((i - 1, j + 1))
                if i != self.size - 1 and (i + 1, j) not in self.walls:
                    self.graph[(i, j)].append((i + 1, j))
                    if j != 0 and (i + 1, j - 1) not in self.walls:
                        self.graph[(i, j)].append((i + 1, j - 1))
                    if j != self.size - 1 and (i + 1, j + 1) not in self.walls: 
                        self.graph[(i, j)].append((i + 1, j + 1))
                if j != 0 and (i, j - 1) not in self.walls:
                    self.graph[(i, j)].append((i, j - 1))
                if j != self.size - 1 and (i, j + 1) not in self.walls:
                    self.graph[(i, j)].append((i, j + 1))
            
        
    def solve(self, algorithm, start, end):
        if self.step == True:
            self.draw(algorithm(self.graph, start, end, self.draw))
        else:
            self.draw(algorithm(self.graph, start, end))
            
    def add_wall(self, wall):
        self.walls = wall
        for i in wall:
            plt.plot(i[0], i[1], 'go')
            


pathfinder = pathfinder(20)

wall = []
for i in range(5, 15):
    wall.append((10, i))
pathfinder.add_wall(wall)

pathfinder.create_graph()




start_time = time.time()
pathfinder.solve(a_star, (0, 0), (19, 19))
end_time = time.time()



execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")

plt.pause(10)
