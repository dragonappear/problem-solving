# https://www.acmicpc.net/problem/4179
from sys import stdin
from collections import deque
input = stdin.readline


def bfs():
    q = deque()
    for r, c in fire:
        dist1[r][c] = 0
        q.append((r, c))

    while q:
        r, c = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r+dr, c+dc

            if not(0 <= nr < R) or not(0 <= nc < C) or board[nr][nc] == '#' or dist1[nr][nc] > -1:
                continue

            dist1[nr][nc] = dist1[r][c]+1
            q.append((nr, nc))


def solve():
    q = deque([(jr, jc)])
    dist2[jr][jc] = 0

    while q:
        r, c = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r+dr, c+dc

            if not(0 <= nr < R) or not(0 <= nc < C):
                return dist2[r][c]+1

            if board[nr][nc] != '.' or (dist1[nr][nc] > -1 and dist1[nr][nc] <= dist2[r][c]+1) or dist2[nr][nc] > -1:
                continue

            dist2[nr][nc] = dist2[r][c]+1
            q.append((nr, nc))

    return "IMPOSSIBLE"


R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
dist1 = [[-1] * C for _ in range(R)]
dist2 = [[-1] * C for _ in range(R)]

fire = []
jr, jc = 0, 0
for i in range(R):
    for j in range(C):
        if board[i][j] == 'F':
            fire.append((i, j))
        elif board[i][j] == 'J':
            jr, jc = i, j

bfs()
print(solve())
