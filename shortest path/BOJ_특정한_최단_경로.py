# https://www.acmicpc.net/problem/1504
from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
input = stdin.readline
INF = float('inf')


def dijk(st, en):
    dist = {v: INF for v in range(1, V+1)}
    dist[st] = 0
    heap = [(0, st)]

    while heap:
        d, u = heappop(heap)

        if u == en:
            return dist[en]

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[v] < d+w:
                continue
            dist[v] = d+w
            heappush(heap, (d+w, v))

    return INF


V, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

m1, m2 = map(int, input().split())

mid = dijk(m1, m2)
a = dijk(1, m1) + mid + dijk(m2, V)
b = dijk(1, m2) + mid + dijk(m1, V)

rst = min(a, b)

print(rst if rst != INF else -1)
