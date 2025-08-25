# Depth-First-Search Algorithm

def dfs(g, node_types):
    def aux(node, path):
        path.append(node)
        if node_types[node] == "goal":
            return path
        if not g[node]:
            return None
        for nd in g[node]:
            v = aux(nd[0], path)
            if v:
                return v
    return aux(0, [])

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

print(dfs(graph, node_type))
