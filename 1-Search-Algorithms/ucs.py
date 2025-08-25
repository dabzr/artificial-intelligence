# Uniform-Cost-Search Algorithm
from heapq import heappush, heappop

def ucs(g, node_types):
    pq = [(0, 0)]
    path = []
    while True:
        cost, node = heappop(pq)
        path.append(node)
        if node_types[node] == "goal":
            break
        if not g[node]:
            path.pop()
            continue
        for nd, cs in g[node]:
            heappush(pq, (cost+cs, nd))
    return path, cost


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

print(ucs(graph, node_type))
