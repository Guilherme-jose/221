def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def guloso(graph, start, end):
    open_nodes = [start]
    closed_nodes = []
    came_from = {}
    
    while open_nodes:
        current = min(open_nodes, key = lambda x: distance(x, end))
        
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
        
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