# https://www.acmicpc.net/problem/2458
from sys import stdin
from collections import defaultdict
input = stdin.readline
INF = 0


def dfs1(u):
    global cnt

    vis[u] = True
    for v in ins[u]:
        if vis[v]:
            continue
        cnt += 1
        dfs1(v)


def dfs2(u):
    global cnt

    vis[u] = True
    for v in outs[u]:
        if vis[v]:
            continue
        cnt += 1
        dfs2(v)


N, M = map(int, input().split())

ins, outs = defaultdict(list), defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    ins[u-1].append(v-1)
    outs[v-1].append(u-1)


ans = 0
for i in range(N):
    cnt = 0
    vis = [False]*N
    dfs1(i)
    vis = [False]*N
    dfs2(i)
    if cnt == N-1:
        ans += 1

print(ans)
