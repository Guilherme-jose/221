
def dijkstra(graph, star, end, draw):
    open_nodes = [star]
    closed_nodes = []
    came_from = {}
    
    g = {node: float('inf') for node in graph}
    g[star] = 0
    
    while open_nodes:
        current = min(open_nodes, key = lambda x: g[x])
        
        reconstruct = current
        
        
        path = []
        while reconstruct in came_from:
            path.append(reconstruct)
            reconstruct = came_from[reconstruct]
        path.append(star)
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
            
            tentative_g = g[current] + 1
            if tentative_g >= g[neighbor]:
                continue
            
            came_from[neighbor] = current
            g[neighbor] = tentative_g
            
    return None