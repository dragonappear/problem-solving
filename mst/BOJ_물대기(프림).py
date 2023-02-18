# https://www.acmicpc.net/problem/1368
from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
input = stdin.readline


graph = defaultdict(list)
N = int(input())
vis = [False] * (N+1)

for i in range(N):
    w = int(input())
    graph[N].append((i, w))
    graph[i].append((N, w))

t = [list(map(int, input().split())) for _ in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        graph[i].append((j, t[i][j]))
        graph[j].append((i, t[i][j]))

heap = [(0, N)]
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
