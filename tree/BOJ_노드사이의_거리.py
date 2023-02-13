# https://www.acmicpc.net/problem/1240
from sys import stdin, setrecursionlimit
from collections import defaultdict
input = stdin.readline
setrecursionlimit(int(1e9))


def dfs(u):
    for v, w in graph[u]:
        if depth[v] >= 0:
            continue
        depth[v] = depth[u]+1
        parent[v] = u
        dist[v] = w
        dfs(v)


N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(N-1):
    U, V, W = map(int, input().split())
    graph[U].append((V, W))
    graph[V].append((U, W))

depth = [-1]*(N+1)  # depth
parent = [-1]*(N+1)  # 부모노드
dist = [-1]*(N+1)  # 부모노드까지 거리

parent[1] = 1
depth[1] = 0
dist[1] = 0
dfs(1)

for _ in range(M):
    a, b = map(int, input().split())

    dist_a = dist_b = 0
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            dist_a += dist[a]
            a = parent[a]
        else:
            dist_b += dist[b]
            b = parent[b]

    while a != b:
        dist_a += dist[a]
        a = parent[a]
        dist_b += dist[b]
        b = parent[b]

    print(dist_a+dist_b)
