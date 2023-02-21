# https://www.acmicpc.net/problem/17835
from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
input = stdin.readline
INF = float('inf')


def dijkstra():
    while heap:
        w, u = heappop(heap)

        if dist[u] != w:  # 이미 방문
            continue

        for v, d in graph[u]:
            if w+d >= dist[v]:
                continue
            dist[v] = w+d
            heappush(heap, (w+d, v))


mx = idx = -1
N, M, K = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[v].append((u, w))

dist = {v: INF for v in range(1, N+1)}
heap = []
go = set(list(map(int, input().split())))
for dest in go:
    dist[dest] = 0
    heap.append((0, dest))

dijkstra()

mx = idx = -1
for i in range(1, N+1):
    if i in go:
        continue
    if dist[i] > mx:
        mx = dist[i]
        idx = i

print(idx)
print(mx)
