# https://www.acmicpc.net/problem/17142
from sys import stdin
from collections import deque
from itertools import combinations
input = stdin.readline


def bfs():
    global mn

    dist = [[-1] * N for _ in range(N)]
    q = deque()

    for c in comb:
        x, y = c//N, c % N
        dist[x][y] = 0
        q.append((x, y))

    cnt = 0
    while q:
        r, c = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nr, nc = r+dr, c+dc

            if not(0 <= nr < N) or not(0 <= nc < N) or board[nr][nc] == 1 or dist[nr][nc] > -1:
                continue

            q.append((nr, nc))
            dist[nr][nc] = dist[r][c]+1
            if board[nr][nc] == 0:
                cnt += 1

    if cnt == empty:
        tmp = 0
        for r in range(N):
            for c in range(N):
                if board[r][c] == 2:
                    continue
                if dist[r][c] > tmp:
                    tmp = dist[r][c]
        if tmp < mn:
            mn = tmp


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

empty = int(sum(1 for i in range(N) for j in range(N) if board[i][j] == 0))

mn = float('inf')
for comb in combinations([i*N+j for i in range(N) for j in range(N) if board[i][j] == 2], M):
    bfs()

print(mn if mn != float('inf') else -1)
