
from a_star import a_star

graph = {}


for i in range(100):
    for j in range(100):
        graph[(i, j)] = []
        if i != 0:
            graph[(i, j)].append((i - 1, j))
            if j != 0:
                graph[(i, j)].append((i - 1, j - 1))
            if j != 99:
                graph[(i, j)].append((i - 1, j + 1))
        if i != 99:
            graph[(i, j)].append((i + 1, j))
            if j != 0:
                graph[(i, j)].append((i + 1, j - 1))
            if j != 99: 
                graph[(i, j)].append((i + 1, j + 1))
        if j != 0:
            graph[(i, j)].append((i, j - 1))
        if j != 99:
            graph[(i, j)].append((i, j + 1))
        
start = (0, 0)
end = (99, 99)



print(a_star(graph, start, end))