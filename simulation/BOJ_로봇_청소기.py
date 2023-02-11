# https://www.acmicpc.net/problem/14503
from sys import stdin, stdout
input, write = stdin.readline, stdout.write

N, M = map(int, input().split())
R, C, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:

    if not board[R][C]:
        board[R][C] = -1  # 청소

    clean = False
    for _ in range(4):
        D = (D+3) % 4
        if board[R+dir[D][0]][C+dir[D][1]] == 0:  # 청소 가능 체크
            R, C = R+dir[D][0], C+dir[D][1]
            clean = True
            break

    if not clean:
        if board[R-dir[D][0]][C-dir[D][1]] == 1:  # 후진 체크
            break

        R, C = R-dir[D][0], C-dir[D][1]  # 후진

print(sum(1 for i in range(N) for j in range(M) if board[i][j] == -1))
