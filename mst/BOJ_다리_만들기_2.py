# https://www.acmicpc.net/problem/17472
from sys import stdin
from collections import deque
input = stdin.readline


# 1.flood fill
# 2.최단경로구성
# 3.mst

def fill(r, c):
    q = deque([(r, c)])
    country[r][c] = cnt
    while q:
        r, c = q.popleft()
        for dr, dc in dr_dc:
            nr, nc = r+dr, c+dc

            if not(0 <= nr < N) or not(0 <= nc < M) or board[nr][nc] == 0 or country[nr][nc] == cnt:
                continue
            q.append((nr, nc))
            country[nr][nc] = cnt


def update_edge():
    for r in range(N):
        for c in range(M):
            if country[r][c] == 0:
                continue
            now = country[r][c]
            for dr, dc in dr_dc:
                nr, nc = r+dr, c+dc
                dist = 0
                while True:
                    if not(0 <= nr < N) or not(0 <= nc < M):
                        break

                    nxt = country[nr][nc]
                    if nxt == now:
                        break
                    elif nxt == 0:
                        dist += 1
                        nr, nc = nr+dr, nc+dc
                    else:
                        if dist >= 2:
                            edges.add((dist, now, nxt))
                        break


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    x = find(a)
    y = find(b)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dr_dc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cnt = 0
country = [[0] * M for _ in range(N)]
edges = set()

# Step 1
for i in range(N):
    for j in range(M):
        if board[i][j] == 0 or country[i][j] >= 1:
            continue
        cnt += 1
        fill(i, j)
parent = [i for i in range(cnt+1)]

# Step 2
update_edge()

# Step 3
edges = sorted(list(edges))
v = ans = 0
for edge in edges:
    cost, a, b = edge
    if find(a) == find(b):
        continue
    union(a, b)
    v += 1
    ans += cost
    if v == cnt-1:
        break

for i in range(1, cnt + 1):
    find(i)

print(ans if len(set(parent[1:])) == 1 else -1)
