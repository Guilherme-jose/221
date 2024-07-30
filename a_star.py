from matplotlib import pyplot as plt

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(graph, start, end, draw): 
    open_nodes = [start]
    closed_nodes = []
    came_from = {}
    
    g = {node: float('inf') for node in graph}
    g[start] = 0
    f = {node: float('inf') for node in graph}
    f[start] = distance(start, end)
    
    while open_nodes:
        current = min(open_nodes, key = lambda x: f[x])
        
       
        path = []
        reconstruct = current
        while reconstruct in came_from:
            path.append(reconstruct)
            reconstruct = came_from[reconstruct]
        path.append(start)
        path.reverse()
        
        draw(path)
        
        if current == end:
            return path
        
        open_nodes.remove(current)
        closed_nodes.append(current)
        
        for neighbor in graph[current]:
            if neighbor in closed_nodes:
                continue
            
            if neighbor not in open_nodes:
                open_nodes.append(neighbor)
            
            tentative_g = g[current] + distance(current, neighbor)
            if tentative_g >= g[neighbor]:
                continue
            
            came_from[neighbor] = current
            g[neighbor] = tentative_g
            f[neighbor] = g[neighbor] + distance(neighbor, end)
        
            
    return None
