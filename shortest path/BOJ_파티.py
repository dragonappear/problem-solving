# https://www.acmicpc.net/problem/1238
from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
input = stdin.readline
INF = float('inf')


def toX(st):
    dist = {v: INF for v in range(1, N+1)}
    dist[st] = 0
    heap = [(0, st)]

    while heap:
        d, u = heappop(heap)

        if u == X:
            return dist[X]

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[v] < d+w:
                continue
            dist[v] = d+w
            heappush(heap, (d+w, v))
    return INF


def fromX():
    dist = {v: INF for v in range(1, N+1)}
    dist[X] = 0
    heap = [(0, X)]

    while heap:
        d, u = heappop(heap)

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[v] < d+w:
                continue
            dist[v] = d+w
            heappush(heap, (d+w, v))

    return dist


N, M, X = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = fromX()
ans = -1
for i in range(1, N+1):
    if i == X:
        continue
    ans = max(ans, toX(i) + dist[i])

print(ans)
