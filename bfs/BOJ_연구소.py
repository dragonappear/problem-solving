# https://www.acmicpc.net/problem/14502
from sys import stdin, stdout
from itertools import combinations
from collections import deque
input, write = stdin.readline, stdout.write

"""
완전탐색

(64)C(3) * 64 = 41664 * 64 = 2_666_496 통과

"""


def bfs():
    global mx
    virus = [(i, j) for i in range(N) for j in range(M) if board[i][j] == 2]
    dist = [elem[::] for elem in board]
    q = deque(virus)
    while q:
        r, c = q.popleft()
        for dr, dc in dr_dc:
            nr, nc = r+dr, c+dc
            # 인덱스 밖 or 벽이거나 방문했는 경우 pass
            if not(0 <= nr < N) or not(0 <= nc < M) or dist[nr][nc] >= 1:
                continue
            q.append((nr, nc))
            dist[nr][nc] = 2

    mx = max(mx, int(sum(1 for i in range(N)
             for j in range(M) if dist[i][j] == 0)))


mx = float('-inf')
N, M = map(int, input().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
dr_dc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

point = [(i, j) for i in range(N) for j in range(M) if board[i][j] == 0]
for a, b, c in combinations(point, 3):
    board[a[0]][a[1]] = board[b[0]][b[1]] = board[c[0]][c[1]] = 1
    bfs()
    board[a[0]][a[1]] = board[b[0]][b[1]] = board[c[0]][c[1]] = 0

print(mx)
