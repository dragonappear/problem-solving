# https://www.acmicpc.net/problem/18809
from sys import stdin
from collections import deque
from itertools import combinations
input = stdin.readline


def bfs():
    dist = [[-1]*M for _ in range(N)]
    color = [[-1]*M for _ in range(N)]
    q = deque()

    for a in red:
        r, c = place[a]
        dist[r][c] = 0
        color[r][c] = 1
        q.append((r, c))

    for a in green:
        r, c = place[a]
        dist[r][c] = 0
        color[r][c] = 2
        q.append((r, c))

    while q:
        r, c = q.popleft()

        if color[r][c] == 0:
            continue

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r+dr, c+dc

            if not(0 <= nr < N) or not(0 <= nc < M) or board[nr][nc] == 0 or (dist[nr][nc] != -1 and dist[nr][nc] < dist[r][c]+1):
                continue

            if (dist[nr][nc] == dist[r][c]+1):
                if color[nr][nc] != color[r][c]:
                    color[nr][nc] = 0
                else:
                    continue
            else:
                dist[nr][nc] = dist[r][c]+1
                color[nr][nc] = color[r][c]
                q.append((nr, nc))

    return int(sum(1 for i in range(N) for j in range(M) if color[i][j] == 0))


N, M, R, G = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
place = [(i, j) for i in range(N) for j in range(M) if board[i][j] == 2]

ans = float('-inf')
for red in combinations(range(0, len(place)), R):
    for green in combinations([i for i in range(0, len(place)) if i not in red], G):
        ans = max(ans, bfs())

print(ans)
