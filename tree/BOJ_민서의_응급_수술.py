# https://www.acmicpc.net/problem/20955
from sys import stdin, setrecursionlimit
from collections import defaultdict
input = stdin.readline
setrecursionlimit(int(1e9))


def dfs(u, prev):
    global cnt
    vis[u] = True
    for v in graph[u]:
        if vis[v]:
            if not cycle[v] and v != prev:  # 사이클 감지
                cnt += 1
            continue

        dfs(v, u)
    cycle[u] = True


N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

vis = [False] * (N+1)
cycle = [False] * (N+1)
ans = 0  # 연결 요소의 개수
cnt = 0  # 사이클의 개수
for i in range(1, N+1):
    if vis[i]:
        continue

    dfs(i, 0)
    ans += 1

print(ans-1+cnt)
