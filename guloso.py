def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def guloso(graph, start, end, draw):
    open_nodes = [start]
    closed_nodes = []
    came_from = {}
    
    while open_nodes:
        current = min(open_nodes, key = lambda x: distance(x, end))
        
        reconstruct = current
        
        if draw != None or current == end:
            path = []
            reconstruct = current
            while reconstruct in came_from:
                path.append(reconstruct)
                reconstruct = came_from[reconstruct]
            path.append(start)
            if draw != None:
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
            
            came_from[neighbor] = current
            
    return None