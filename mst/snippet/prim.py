from heapq import heappop, heappush


def prim(adj_list):
    visited = set()
    start_vertex = list(adj_list.keys())[0]
    heap = [(0, start_vertex)]
    mst = []

    while heap:
        weight, current_vertex = heappop(heap)

        if current_vertex not in visited:
            visited.add(current_vertex)
            mst.append((weight, current_vertex))

            for neighbor, edge_weight in adj_list[current_vertex]:
                if neighbor not in visited:
                    heappush(heap, (edge_weight, neighbor))

    return mst
