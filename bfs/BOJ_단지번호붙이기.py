# https://www.acmicpc.net/problem/2667
from sys import stdin, stdout
from collections import deque
input, write = stdin.readline, stdout.write


def bfs():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 or dist[i*N+j] > 0:
                continue
            cnt += 1
            q = deque([(i, j)])
            dist[i*N+j] = cnt
            while q:
                r, c = q.popleft()
                for dr, dc in dr_dc:
                    nr, nc = r+dr, c+dc
                    if not(0 <= nr < N) or not(0 <= nc < N) or board[nr][nc] == 0:
                        continue
                    if dist[nr*N+nc] > 0:
                        continue
                    q.append((nr, nc))
                    dist[nr*N+nc] = cnt
    return cnt


N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]
dr_dc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dist = [-1]*(N*N)
tot = bfs()

print(tot)
arr = [0] * (tot+1)
for i in range(N*N):
    if dist[i] > 0:
        arr[dist[i]] += 1

arr.sort()

for i in range(1, tot+1):
    print(arr[i])
