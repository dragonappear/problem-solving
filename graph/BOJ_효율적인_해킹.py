# https://www.acmicpc.net/problem/1325
from sys import stdin
from collections import defaultdict, deque
input = stdin.readline


def bfs(u):
    vis = [False] * (N+1)

    q = deque([u])
    vis[u] = True
    cnt = 1

    while q:
        u = q.popleft()

        for v in graph[u]:
            if vis[v]:
                continue
            cnt += 1
            vis[v] = True
            q.append(v)

    return cnt


N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[v].append(u)

arr = [0] * (N+1)
mx = -1
for i in range(1, N+1):
    arr[i] = bfs(i)
    if mx < arr[i]:
        mx = arr[i]

print(*[i for i in range(1, N+1) if arr[i] == mx])
