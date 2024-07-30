
from a_star import a_star



class pathfinder:
    graph = {}
    
    def create_graph(self):
        for i in range(100):
            for j in range(100):
                self.graph[(i, j)] = []
                if i != 0:
                    self.graph[(i, j)].append((i - 1, j))
                    if j != 0:
                        self.graph[(i, j)].append((i - 1, j - 1))
                    if j != 99:
                        self.graph[(i, j)].append((i - 1, j + 1))
                if i != 99:
                    self.graph[(i, j)].append((i + 1, j))
                    if j != 0:
                        self.graph[(i, j)].append((i + 1, j - 1))
                    if j != 99: 
                        self.graph[(i, j)].append((i + 1, j + 1))
                if j != 0:
                    self.graph[(i, j)].append((i, j - 1))
                if j != 99:
                    self.graph[(i, j)].append((i, j + 1))
            
        
    def solve(self, algorithm, start, end):
        algorithm(self.graph, start, end)
        
        
pathfinder = pathfinder()

pathfinder.create_graph()

pathfinder.solve(a_star, (0, 0), (99, 99))