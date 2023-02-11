# https://www.acmicpc.net/problem/14500
from sys import stdin, stdout
input, write = stdin.readline, stdout.write


def dfs(r, c, cnt, tot):
    global mx
    if cnt == 4:
        mx = max(tot, mx)
        return

    for dr, dc in dr_dc:
        nr, nc = r+dr, c+dc
        if not(0 <= nr < N) or not(0 <= nc < M) or vis[nr][nc]:
            continue

        vis[nr][nc] = True
        dfs(nr, nc, cnt+1, tot+board[nr][nc])
        if cnt == 2:
            dfs(r, c, cnt+1, tot+board[nr][nc])
        vis[nr][nc] = False


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
vis = [[False]*M for _ in range(N)]
dr_dc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
mx = float('-inf')

for i in range(N):
    for j in range(M):
        vis[i][j] = True
        dfs(i, j, 1, board[i][j])
        vis[i][j] = False

print(mx)
