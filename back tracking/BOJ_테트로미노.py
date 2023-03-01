# https://www.acmicpc.net/problem/14500
from sys import stdin
input = stdin.readline


def dfs(r, c, cnt, sm):
    global mx

    if cnt == 4:
        mx = max(mx, sm)
        return

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r+dr, c+dc

        if not(0 <= nr < N) or not(0 <= nc < M) or vis[nr][nc]:
            continue

        vis[nr][nc] = True
        dfs(nr, nc, cnt+1, sm+board[nr][nc])
        if cnt == 2:
            dfs(r, c, cnt+1, sm+board[nr][nc])
        vis[nr][nc] = False


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
vis = [[False] * M for _ in range(N)]
mx = float('-inf')

for i in range(N):
    for j in range(M):
        vis[i][j] = True
        dfs(i, j, 1, board[i][j])
        vis[i][j] = False

print(mx)
