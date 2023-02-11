# https://www.acmicpc.net/problem/14502
from sys import stdin, stdout
from collections import deque
from itertools import combinations
input, write = stdin.readline, stdout.write


def bfs():
    global mx
    vis = [[False]*M for _ in range(N)]
    for r, c in virus:
        vis[r][c] = True
    q = deque(virus)
    while q:
        r, c = q.popleft()
        for dr, dc in dr_dc:
            nr, nc = r+dr, c+dc
            if not(0 <= nr < N) or not(0 <= nc < M) or vis[nr][nc] or board[nr][nc] == 1:
                continue
            vis[nr][nc] = True
            q.append((nr, nc))

    cnt = int(sum(1 for i in range(N)
              for j in range(M) if not vis[i][j] and board[i][j] != 1))
    mx = max(cnt, mx)
    return


N, M = map(int, input().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
virus = [(i, j) for i in range(N) for j in range(M) if board[i][j] == 2]
dr_dc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

mx = float('-inf')
for combi in combinations([i for i in range(N*M) if board[i//M][i % M] == 0], 3):
    carr = [(c//M, c % M) for c in combi]
    for r, c in carr:
        board[r][c] = 1
    bfs()
    for r, c in carr:
        board[r][c] = 0

print(mx)
