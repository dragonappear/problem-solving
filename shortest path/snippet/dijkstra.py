from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
input = stdin.readline

# O(ElogE)
V, E = map(int, input().split())
START = int(input())
graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().strip().split())
    graph[u].append((v, w))

dist = {v: float('inf') for v in range(1, V+1)}
dist[START] = 0
heap = [(0, START)]

while heap:
    d, u = heappop(heap)

    if d > dist[u]:
        continue

    for v, w in graph[u]:
        if d+w < dist[v]:
            dist[v] = d+w
            heappush(heap, (d+w, v))
