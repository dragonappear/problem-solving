# https://www.acmicpc.net/problem/6118
from sys import stdin
from collections import defaultdict, deque
input = stdin.readline


def bfs():
    dist[1] = 0
    q = deque([1])
    while q:
        u = q.popleft()

        for v in graph[u]:
            if dist[v] >= 0:
                continue

            dist[v] = dist[u]+1
            q.append(v)


N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dist = [-1] * (N+1)
bfs()

rst = [-1, 0, 0]
mx = max(dist)
rst[1] = mx
for i in range(1, N+1):
    if dist[i] == mx:
        rst[2] += 1
        if rst[0] == -1:
            rst[0] = i

print(*rst)
