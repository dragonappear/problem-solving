# https://www.acmicpc.net/problem/6087
from sys import stdin
from collections import deque
input = stdin.readline
INF = float('inf')

W, H = map(int, input().split())
board = list(list(input().strip()) for _ in range(H))
dist = [[INF] * W for _ in range(H)]

c = [(i, j) for i in range(H) for j in range(W) if board[i][j] == 'C']
(sr, sc), (er, ec) = c[0], c[1]

dist[sr][sc] = 0
q = deque([(sr, sc, 0)])

while q:
    r, c, m = q.popleft()

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r+dr, c+dc

        while (0 <= nr < H) and (0 <= nc < W) and board[nr][nc] != "*":
            if dist[nr][nc] > m:
                dist[nr][nc] = m
                q.append((nr, nc, m+1))
            nr, nc = nr+dr, nc+dc

print(dist[er][ec])
