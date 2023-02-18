# https://www.acmicpc.net/problem/1197
from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop
input = stdin.readline

V, E = map(int, input().split())
graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

vis = [False] * (V+1)
heap = [(0, 1)]  # 출발정점:1

ans = 0
while heap:
    weight, u = heappop(heap)
    if vis[u]:
        continue

    vis[u] = True
    ans += weight

    for v, w in graph[u]:
        if not vis[v]:
            heappush(heap, (w, v))

print(ans)
