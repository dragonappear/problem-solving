# https://www.acmicpc.net/problem/14442
from sys import stdin
from collections import deque
input = stdin.readline


def bfs():
    dist = [[[-1]*M for _ in range(N)] for _ in range(K+1)]
    q = deque([(0, 0, 0)])
    dist[0][0][0] = 0

    while q:
        k, r, c = q.popleft()

        if (r, c) == (N-1, M-1):
            return dist[k][r][c]+1

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r+dr, c+dc

            if not(0 <= nr < N) or not(0 <= nc < M):
                continue

            if board[nr][nc] == 0:
                if dist[k][nr][nc] >= 0:
                    continue
                else:
                    dist[k][nr][nc] = dist[k][r][c]+1
                    q.append((k, nr, nc))
            else:
                if k+1 <= K and dist[k+1][nr][nc] == -1:
                    dist[k+1][nr][nc] = dist[k][r][c]+1
                    q.append((k+1, nr, nc))

    return -1


N, M, K = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
print(bfs())
