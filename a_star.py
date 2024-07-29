from draw import draw

def a_star(graph, start, end): 
    open_nodes = [start]
    closed_nodes = []
    came_from = {}
    
    g = {node: float('inf') for node in graph}
    g[start] = 0
    f = {node: float('inf') for node in graph}
    f[start] = distance(start, end)
    
    while open_nodes:
        current = min(open_nodes, key = lambda x: f[x])
        
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            
            draw(path)
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