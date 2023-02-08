# https://www.acmicpc.net/problem/7569
from sys import stdin, stdout
from collections import deque
input, write = stdin.readline, stdout.write


def bfs():
    q = deque()
    dist = [[[-1]*M for _ in range(N)] for _ in range(H)]

    for k in range(H):
        for i in range(N):
            for j in range(M):
                if board[k][i][j] == -1:
                    dist[k][i][j] = 0
                elif board[k][i][j] == 1:
                    dist[k][i][j] = 0
                    q.append((k, i, j))

    while q:
        h, r, c = q.popleft()
        for dr, dc, dh in dr_dc_dh:
            nh, nr, nc = h+dh, r+dr, c+dc
            if not(0 <= nh < H) or not(0 <= nr < N) or not(0 <= nc < M):
                continue
            if dist[nh][nr][nc] >= 0 or board[nh][nr][nc] == -1:
                continue
            dist[nh][nr][nc] = dist[h][r][c]+1
            q.append((nh, nr, nc))

    ans = 0
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if dist[k][i][j] == -1:
                    return -1
                elif dist[k][i][j] > 0:
                    ans = max(ans, dist[k][i][j])
    return ans


M, N, H = map(int, input().split())
board = [[list(map(int, input().split()))
         for _ in range(N)] for _ in range(H)]  # 0: 익X토 , 1: 익O토, -1: 빈 칸
dr_dc_dh = [(0, 1, 0), (0, -1, 0), (1, 0, 0),
            (-1, 0, 0), (0, 0, 1), (0, 0, -1)]
print(bfs())
