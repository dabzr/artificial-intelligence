# Iterative-Deepening-Search Algorithm

def ids(g, node_types):
    def aux(node, path, count, max):
        path.append(node)
        if node_types[node] == "goal":
            return path
        if not g[node]:
            return None
        if count + 1 == max:
            return path
        for nd in g[node]:
            v = aux(nd[0], path, count+1, max)
            if v:
                return v
    while True:
        aux(0, [], 0, 1)

# WORK IN PROGRESS
