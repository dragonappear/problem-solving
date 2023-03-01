# https://www.acmicpc.net/problem/2583
from sys import stdin
from collections import deque
input = stdin.readline


def bfs(i, j):
    q = deque([(i, j)])
    board[i][j] = 1
    cnt = 1
    while q:
        r, c = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nr, nc = r+dr, c+dc
            if not(0 <= nr < M) or not(0 <= nc < N) or board[nr][nc] == 1:
                continue

            board[nr][nc] = 1
            cnt += 1
            q.append((nr, nc))

    return cnt


N, M, K = map(int, input().split())
board = [[0] * N for _ in range(M)]

for _ in range(K):
    a, b, c, d = map(int, input().split())

    for i in range(a, c):
        for j in range(b, d):
            board[i][j] = 1

rst = []
for i in range(M):
    for j in range(N):
        if board[i][j]:
            continue

        rst.append(bfs(i, j))

print(len(rst))
print(*sorted(rst))
