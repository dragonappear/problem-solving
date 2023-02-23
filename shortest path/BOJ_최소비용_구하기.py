# https://www.acmicpc.net/problem/1916
from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
input = stdin.readline
INF = float('inf')


def dijk(st, en):
    d = {v: INF for v in range(1, N+1)}
    d[st] = 0
    heap = [(0, st)]

    while heap:
        c, u = heappop(heap)

        if u == en:
            return d[en]

        if d[u] < c:
            continue

        for v, w in graph[u]:
            if d[v] > c+w:
                d[v] = c+w
                heappush(heap, (c+w, v))


N = int(input())
graph = defaultdict(list)
for _ in range(int(input())):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

st, en = map(int, input().split())

print(dijk(st, en))
