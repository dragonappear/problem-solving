# https://www.acmicpc.net/problem/7576
from sys import stdin, stdout
from collections import deque
input, write = stdin.readline, stdout.write


def bfs():
    q = deque()
    dist = [[-1]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == -1:
                dist[i][j] = 0
            elif board[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))

    while q:
        r, c = q.popleft()
        for dr, dc in dr_dc:
            nr, nc = r+dr, c+dc
            if not(0 <= nr < N) or not(0 <= nc < M) or dist[nr][nc] >= 0 or board[nr][nc] == -1:
                continue
            dist[nr][nc] = dist[r][c]+1
            q.append((nr, nc))

    ans = 0
    for i in range(N):
        for j in range(M):
            if dist[i][j] == -1:
                return -1
            elif dist[i][j] > 0:
                ans = max(ans, dist[i][j])

    return ans


M, N = map(int, input().split())
board = [list(map(int, input().split()))
         for _ in range(N)]  # 0: 익X토 , 1: 익O토, -1: 빈 칸
dr_dc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
print(bfs())
