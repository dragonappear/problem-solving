# https://www.acmicpc.net/problem/14500
from sys import stdin, stdout
input, write = stdin.readline, stdout.write

tetro = [
    # 하늘
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],

    # 노란
    [(0, 0), (0, 1), (1, 0), (1, 1)],

    # 주황
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 0)],

    [(0, 1), (1, 1), (2, 1), (0, 0)],
    [(0, 1), (1, 1), (2, 1), (2, 0)],
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],

    # 초록
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (0, 1), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 1), (1, 1), (1, 0), (2, 0)],

    # 자주
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(1, 0), (1, 1), (1, 2), (0, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 1), (1, 1), (2, 1), (1, 0)]
]


def solve(r, c):
    tot = 0
    for i in range(19):
        sum = 0
        for j in range(4):
            sum += board[r+tetro[i][j][0]][c+tetro[i][j][1]]
        tot = max(tot, sum)
    return tot


N, M = map(int, input().split())

board = [[0]*505 for _ in range(505)]
for i in range(N):
    board[i] = list(map(int, input().split()))+[0]*(505-M)

mx = 0
for i in range(N):
    for j in range(M):
        mx = max(mx, solve(i, j))
print(mx)
