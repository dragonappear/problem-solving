# https://www.acmicpc.net/problem/11438
from sys import stdin, setrecursionlimit
from collections import defaultdict
input = stdin.readline
setrecursionlimit(int(1e9))
LOG = 21


def set_parent():
    vis[1] = True
    d[1] = 0
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]


def dfs(u, depth):
    for v in graph[u]:
        if vis[v]:
            continue
        vis[v] = True
        d[v] = depth+1
        parent[v][0] = u
        dfs(v, depth+1)


def lca(a, b):  # A와 B의 LCA
    if d[a] > d[b]:  # b가 더 깊도록 설정
        a, b = b, a

    for i in range(LOG-1, -1, -1):  # 깊이 동일하도록 설정
        if d[b]-d[a] >= (1 << i):
            b = parent[b][i]

    if a == b:
        return a

    for i in range(LOG-1, -1, -1):  # 조상 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]


N = int(input())
parent = [[0] * LOG for _ in range(N+1)]
d = [0] * (N+1)
vis = [0] * (N+1)
graph = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

set_parent()

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lca(a, b))
