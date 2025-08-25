# Breadth-First-Search Algorithm

def bfs(g, node_types, start=0):
    start = start
    q = [start]
    path = []
    visited = set([start])
    parent: dict[int, None | int] = {start: None} 
    while True:
        node = q.pop(0)
        path.append(node)
        if node_types[node] == "goal":
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            break
        if not g[node]:
           path.pop()
           continue
        for child, _ in g[node]:
            if child not in visited:
                visited.add(child)
                parent[child] = node
                q.append(child)
    return path[::-1]

graph = {
    0: [(1, 5), (2, 2)],
    1: [(2, 1)],
    2: [(3, 7)],
    3: []
}

node_type = {
    0: "start",
    1: "normal",
    2: "goal",
    3: "normal"
}

print(bfs(graph, node_type))
