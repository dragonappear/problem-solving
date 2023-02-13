# https://www.acmicpc.net/problem/15681
from sys import stdin, setrecursionlimit
from collections import defaultdict
input = stdin.readline
setrecursionlimit(int(1e9))


def set_child_cnt(u):
    for v in graph[u]:
        if vis[v]:
            continue
        vis[v] = True
        child_cnt[u] += set_child_cnt(v)

    return child_cnt[u]


N, R, Q = map(int, input().split())
graph = defaultdict(list)

for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

child_cnt = [1] * (N+1)
vis = [False]*(N+1)
vis[R] = True
set_child_cnt(R)
for _ in range(Q):
    print(child_cnt[int(input())])
