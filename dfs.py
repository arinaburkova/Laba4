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




if __name__ == "__main__":
    edges = [(4, 2), (1, 3), (2, 4)]
    graph = build_graph(edges)
    print("DFS traversal starting from 1:", dfs(graph, 1))  # [1, 3]
    print("Path length from 2 to 4:", dfs_path_length(graph, 2, 4))  # 1

