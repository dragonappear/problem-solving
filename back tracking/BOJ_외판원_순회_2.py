# https://www.acmicpc.net/problem/10971
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(int(1e9))


def dfs(st, u, sm, cnt):
    global mn

    if cnt == N-1:
        if W[u][st] and sm+W[u][st] < mn:
            mn = sm+W[u][st]
        return

    for i in range(N):
        if vis[i] or W[u][i] == 0:
            continue

        tmp = sm+W[u][i]
        if tmp < mn:
            vis[i] = True
            dfs(st, i, tmp, cnt+1)
            vis[i] = False


N = int(input())
vis = [False] * N
W = [list(map(int, input().strip().split())) for _ in range(N)]

mn = float('inf')

for i in range(N):
    vis[i] = True
    dfs(i, i, 0, 0)
    vis[i] = False

print(mn)
