# https://www.acmicpc.net/problem/1600
from sys import stdin
from collections import deque
input = stdin.readline


def bfs():

    if board[0][0] == 1:
        return -1

    dist = [[[-1] * W for _ in range(H)] for _ in range(K+1)]
    q = deque([(0, 0, 0)])
    dist[0][0][0] = 0

    while q:
        r, c, k = q.popleft()

        if (r, c) == (H-1, W-1):
            return dist[k][r][c]

        if k < K:
            for dr, dc in [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]:
                nr, nc = r+dr, c+dc

                if not(0 <= nr < H) or not(0 <= nc < W) or board[nr][nc] or dist[k+1][nr][nc] > -1:
                    continue

                dist[k+1][nr][nc] = dist[k][r][c]+1
                q.append((nr, nc, k+1))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r+dr, c+dc

            if not(0 <= nr < H) or not(0 <= nc < W) or board[nr][nc] or dist[k][nr][nc] > -1:
                continue

            dist[k][nr][nc] = dist[k][r][c]+1
            q.append((nr, nc, k))

    return -1


K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
print(bfs())
