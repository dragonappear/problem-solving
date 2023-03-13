# https://www.acmicpc.net/problem/17182
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(int(1e9))
INF = float('inf')


def dfs(st, dist, cnt):
    global ans

    if ans < dist:
        return

    if cnt == N:
        ans = min(ans, dist)
        return

    for en in range(N):
        if vis[en]:
            continue

        vis[en] = True
        dfs(en, dist+board[st][en], cnt+1)
        vis[en] = False


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]

ans = float('inf')
vis = [False] * N
vis[K] = True
dfs(K, 0, 1)

print(ans)
