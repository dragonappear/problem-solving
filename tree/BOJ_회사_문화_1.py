# https://www.acmicpc.net/problem/14267
from sys import stdin, setrecursionlimit
from collections import defaultdict
input = stdin.readline
setrecursionlimit(int(1e9))


def dfs(u, w):
    tot[u] += w
    for v in graph[u]:
        dfs(v, w+cnt[v])


N, M = map(int, input().split())
parent = list(map(int, input().split()))
graph = defaultdict(list)
for i, v in enumerate(parent):
    if v != -1:
        graph[v].append(i+1)

cnt = [0]*(N+1)
tot = [0]*(N+1)
for _ in range(M):
    I, W = map(int, input().split())
    cnt[I] += W

dfs(1, cnt[1])

print(*[tot[i] for i in range(1, N+1)])
