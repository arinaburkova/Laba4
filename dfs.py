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
#comment1
#comment2


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
def dfs_path_length1111111(graph, start, end):
    pass
def dfs_path_length(graph, start, end):
  
#new comment

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
    Модернизированная функция поиска длины пути DFS
    Добавлены проверки входных данных и обработка ошибок
    """
    # Валидация входного графа
    if not graph or not isinstance(graph, dict):
        raise ValueError("Некорректный формат графа")
    
    # Проверка существования вершин в графе
    if start not in graph:
        raise ValueError(f"Стартовая вершина {start} отсутствует в графе")
    if end not in graph:
        raise ValueError(f"Конечная вершина {end} отсутствует в графе")
    
    # Особый случай: начальная и конечная вершины совпадают
    if start == end:
        return 0


if __name__ == "__main__":
    edges = [(4, 2), (1, 3), (2, 4)]
    graph = build_graph(edges)
    print("DFS traversal starting from 1:", dfs(graph, 1))  # [1, 3]
    print("Path length from 2 to 4:", dfs_path_length(graph, 2, 4))  # 1

