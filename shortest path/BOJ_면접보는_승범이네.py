# https://www.acmicpc.net/problem/17835
from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
input = stdin.readline
INF = float('inf')


def dijk():
    global mx, idx
    dist = [INF] * (N+1)
    heap = []

    for c in city:
        heap.append((0, c))
        dist[c] = 0

    while heap:
        d, u = heappop(heap)

        if dist[u] < d:
            continue

        for v, w in graph[u]:
            if dist[v] < d+w:
                continue

            dist[v] = d+w
            heappush(heap, (d+w, v))

    for i in range(1, N+1):
        if i in city:
            continue

        if mx < dist[i]:
            mx = dist[i]
            idx = i


N, M, K = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[v].append((u, w))

city = set(list(map(int, input().split())))
mx = float('-inf')
idx = -1

dijk()

print(idx)
print(mx)
