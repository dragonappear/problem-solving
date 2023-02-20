def bellman_ford(graph, source):
    # initialize distances and predecessors
    dist = {v: float('inf') for v in graph}
    dist[source] = 0
    pred = {v: None for v in graph}

    # relax edges repeatedly
    for i in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    pred[v] = u

    # check for negative cycles
    for u in graph:
        for v, w in graph[u].items():
            if dist[u] + w < dist[v]:
                raise ValueError("graph contains a negative-weight cycle")

    return dist, pred
