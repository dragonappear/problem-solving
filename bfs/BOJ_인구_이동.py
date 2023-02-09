# https://www.acmicpc.net/problem/16234
from sys import stdin, stdout
from collections import deque
input, write = stdin.readline, stdout.write


def bfs():
    move = False
    vis = [[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if vis[i][j]:
                continue

            q = deque([(i, j)])
            vis[i][j] = True
            tot = board[i][j]
            trace = [(i, j)]

            while q:
                r, c = q.popleft()
                for dr, dc in dr_dc:
                    nr, nc = r+dr, c+dc
                    if not(0 <= nr < N) or not(0 <= nc < N) or vis[nr][nc]:
                        continue
                    if not(L <= abs(board[nr][nc]-board[r][c]) <= R):
                        continue

                    vis[nr][nc] = True
                    q.append((nr, nc))
                    trace.append((nr, nc))
                    tot += board[nr][nc]

            if len(trace) >= 2:
                move = True
                rst = tot//len(trace)
                for a, b in trace:
                    board[a][b] = rst

    if not move:
        return False
    return True


N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dr_dc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = 0

while True:
    if not bfs():
        break
    ans += 1

print(ans)
