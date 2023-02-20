# https://www.acmicpc.net/problem/1753
from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
input = stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().strip().split())
    graph[u].append((v, w))

dist = defaultdict(int)
heap = [(0, K)]

while heap:
    d, u = heappop(heap)
    if u not in dist:
        dist[u] = d
        for v, w in graph[u]:
            heappush(heap, (d+w, v))

for i in range(1, V+1):
    print(dist[i] if i in dist else "INF")
