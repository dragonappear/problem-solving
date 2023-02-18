import heapq


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def prim(self, start_vertex):
        visited = [False] * self.num_vertices
        min_heap = [(0, start_vertex)]
        total_weight = 0

        while min_heap:
            weight, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            total_weight += weight

            for v, weight in self.adj_list[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (weight, v))

        return total_weight
