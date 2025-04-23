def dfs(graph, start):
    
    visited = set()
    stack = [start]
    traversal_order = []
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal_order.append(vertex)
           
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return traversal_order


def build_graph(edges):
   
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    return graph

def dfs_path_length(graph, start, end):
  

    if start == end:
        return 0
    
    visited = set()
    stack = [(start, 0)]  # (vertex, distance)
    
    while stack:
        vertex, distance = stack.pop()
        if vertex == end:
            return distance
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append((neighbor, distance + 1))
    
    return -1
def dfs_path_length(graph, start, end):
    """
    [Previous docstring remains...]
    """
    # Validate input graph
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Check if nodes exist in graph
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")
    if end not in graph:
        raise ValueError(f"End node {end} not found in graph")
    
    # Special case: start == end
    if start == end:
        return 0
    
    # DFS implementation with distance tracking
    visited = set()  # To keep track of visited nodes
    stack = [(start, 0)]  # Stack stores tuples of (node, distance)
    
    while stack:
        vertex, distance = stack.pop()
        
        # Check if we've reached the target
        if vertex == end:
            return distance
            
        if vertex not in visited:
            visited.add(vertex)
            # Add neighbors to stack in reverse order
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append((neighbor, distance + 1))
    
    return -1  # Indicates no path found


if __name__ == "__main__":
    edges = [(4, 2), (1, 3), (2, 4)]
    graph = build_graph(edges)
    print("DFS traversal starting from 1:", dfs(graph, 1))  # [1, 3]
    print("Path length from 2 to 4:", dfs_path_length(graph, 2, 4))  # 1

