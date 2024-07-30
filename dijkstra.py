
def dijkstra(graph, star, end):
    open_nodes = [star]
    closed_nodes = []
    came_from = {}
    
    g = {node: float('inf') for node in graph}
    g[star] = 0
    
    while open_nodes:
        current = min(open_nodes, key = lambda x: g[x])
        
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(star)
            path.reverse()
            
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