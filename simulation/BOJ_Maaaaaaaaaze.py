# https://www.acmicpc.net/problem/16985
from sys import stdin, stdout
from collections import deque
from itertools import permutations, product
input, write = stdin.readline, stdout.write


def solve():
    dist = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    q = deque([(0, 0, 0)])
    dist[0][0][0] = 1

    while q:
        r, c, h = q.popleft()

        for dr, dc, dh in dr_dc_dh:
            nr, nc, nh = r+dr, c+dc, h+dh

            if not(0 <= nr < 5) or not(0 <= nc < 5) or not(0 <= nh < 5):
                continue
            if maze[nr][nc][nh] == 0 or dist[nr][nc][nh] != 0:
                continue
            if nr == 4 and nc == 4 and nh == 4:
                return dist[r][c][h]

            dist[nr][nc][nh] = dist[r][c][h]+1
            q.append((nr, nc, nh))

    return float('inf')


# board[dir][i][j][k]: i번째 판을 시계방향으로 dir번 돌렸을때 (j,k)의 값
board = [[[[0]*5 for _ in range(5)] for _ in range(5)] for _ in range(4)]
maze = [[[0] * 5 for _ in range(5)] for _ in range(5)]
dr_dc_dh = [(1, 0, 0), (0, 1, 0), (0, -1, 0),
            (0, 0, 1), (0, 0, -1), (-1, 0, 0)]

for i in range(5):
    for j in range(5):
        board[0][i][j] = list(map(int, input().strip().split()))

    for j in range(5):
        for k in range(5):
            board[1][i][j][k] = board[0][i][4-k][j]

    for j in range(5):
        for k in range(5):
            board[2][i][j][k] = board[1][i][4-k][j]

    for j in range(5):
        for k in range(5):
            board[3][i][j][k] = board[2][i][4-k][j]

ans = float('inf')
for order in permutations([i for i in range(5)]):  # 판 쌓는 순서
    # for tmp in range(1024):
    #     brute = tmp  # 5개의 판에 대해 dir을 정해주기 위한 변수
    #     for i in range(5):
    #         # dir = brute & 3
    #         dir = brute % 4
    #         # brute >>= 2
    #         brute //= 4
    #         for j in range(5):
    #             for k in range(5):
    #                 maze[i][j][k] = board[dir][order[i]][j][k]
    for dir in product([i for i in range(4)], repeat=5):  # 판 회전
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    maze[i][j][k] = board[dir[i]][order[i]][j][k]

        if maze[0][0][0] == 0 or maze[4][4][4] == 0:
            continue

        ans = min(ans, solve())

print(ans if ans != float('inf') else -1)
