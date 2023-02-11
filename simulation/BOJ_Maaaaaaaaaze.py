# https://www.acmicpc.net/problem/16985
from sys import stdin, stdout
from collections import deque
from itertools import permutations
input, write = stdin.readline, stdout.write


def bfs():
    global mn
    dist = [[[-1]*5 for _ in range(5)] for _ in range(5)]

    dist[0][0][0] = 0
    q = deque([(0, 0, 0)])

    while q:
        r, c, h = q.popleft()

        for dr, dc, dh in dr_dc_dh:
            nr, nc, nh = r+dr, c+dc, h+dh

            if not(0 <= nr < 5) or not(0 <= nc < 5) or not(0 <= nh < 5):
                continue

            if maze[nr][nc][nh] == 0 or dist[nr][nc][nh] != -1:
                continue

            if (nr, nc, nh) == (4, 4, 4):
                mn = min(mn, dist[r][c][h]+1)
                return

            dist[nr][nc][nh] = dist[r][c][h]+1
            q.append((nr, nc, nh))


def rotate(k, n):
    tmp = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            tmp[i][j] = board[k][n][4-j][i]
    return tmp


mn = float('inf')
# board[k][n][i][j] = k: 회전횟수 , n:번째, (i,j):행열
board = [[[[0]*5 for _ in range(5)] for _ in range(5)] for _ in range(4)]
dr_dc_dh = [(1, 0, 0), (-1, 0, 0), (0, 1, 0),
            (0, -1, 0), (0, 0, 1), (0, 0, -1)]
maze = [[] for _ in range(5)]

# 회전 셋업
for i in range(5):
    for j in range(5):
        board[0][i][j] = list(map(int, input().strip().split()))
    for k in range(1, 4):
        board[k][i] = rotate(k-1, i)


# 탑쌓기
for order in permutations([i for i in range(5)]):
    # 회전
    for tmp in range(1024):
        brute = tmp
        for i in range(5):
            dir = brute & 3
            brute >>= 2
            maze[i] = (board[dir][order[i]])

        if maze[0][0][0] == 0 or maze[4][4][4] == 0:
            continue
        bfs()

print(mn if mn != float('inf') else -1)
