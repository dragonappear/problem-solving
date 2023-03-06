# https://www.acmicpc.net/problem/24042
from sys import stdin
from heapq import heappop, heappush
from collections import defaultdict
input = stdin.readline
INF = float('inf')


def dijk():
    d = [INF]*(N+1)
    d[1] = 0
    heap = [(0, 1)]  # (t,i) : i번째 노드까지 가는데 걸리는 시간

    while heap:
        c, u = heappop(heap)  # c: 현재 시간,u: 현재 위치

        if d[u] < c:
            continue

        for v, t in graph[u]:
            w = c + (t-c) % M  # w: u에서 v까지 가는데 걸리는 시간

            if d[v] < w+1:
                continue

            d[v] = w+1
            heappush(heap, (w+1, v))

    return d[N]


N, M = map(int, input().split())
graph = defaultdict(list)
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append((v, i))
    graph[v].append((u, i))

print(dijk())
